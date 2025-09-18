# -*- coding: utf-8 -*-

"""
Gmail API Pagination Utilities

This module provides pagination utilities for Gmail API list operations.
It abstracts the complexity of handling pageToken and nextPageToken to
provide a simple iterator interface for paginated API responses.

The module follows the adapter pattern to handle different Gmail API
endpoints (messages, threads) with a unified pagination mechanism.
"""

import typing as T

from .paginate import paginate
from .model import ListMessagesResponse
from .iterator import ListMessagesResponseIterProxy
from .model import ListThreadsResponse
from .iterator import ListThreadsResponseIterProxy

if T.TYPE_CHECKING:
    from googleapiclient._apis.gmail.v1 import GmailResource


def pagi_list_messages(
    gmail: "GmailResource",
    kwargs: dict[str, T.Any] | None = None,
    page_size: int = 100,
    max_items: int = 1000,
) -> ListMessagesResponseIterProxy:
    """
    Paginated Gmail messages list with automatic token handling.

    Provides a convenient iterator interface for Gmail's messages.list API,
    automatically handling pagination tokens and respecting limits. Each
    iteration yields a complete API response containing a batch of messages.

    :param gmail: Gmail API client resource
    :param kwargs: Parameters for
        `messages.list <https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list>`_
    :param page_size: Number of messages per API request (maxResults)
    :param max_items: Maximum total messages to return across all pages

    :yields: API response dictionaries, each containing a 'messages' list

    Example:
        Listing recent messages with custom page size::

            for response in page_list_messages(
                client=gmail_client,
                kwargs={"userId": "me", "q": "is:unread"},
                page_size=50,
                max_items=200
            ):
                messages = response.get("messages", [])
                print(f"Processing {len(messages)} messages")
                for msg in messages:
                    print(f"Message ID: {msg['id']}")

    .. note::
        This function only returns message metadata (ID and threadId).
        Use messages.get API to retrieve full message content.
    """
    if kwargs is None:
        kwargs = {}

    # Set the page size for each API request
    kwargs["maxResults"] = page_size

    paginator = paginate(
        method=gmail.users().messages().list,
        items_field="messages",
        kwargs=kwargs,
        max_items=max_items,
    )

    return ListMessagesResponseIterProxy.from_paginator(paginator, ListMessagesResponse)
