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

from .type_hint import T_KWARGS, T_RESPONSE


def default_set_page_size(
    request_kwargs: T_KWARGS,
    page_size: int,
):
    """
    Set maxResults in request parameters for page size.
    """
    request_kwargs["maxResults"] = page_size


def default_get_next_token(
    response: T_RESPONSE,
) -> str | None:
    """
    Extract nextPageToken from Gmail API response.
    """
    return response.get("nextPageToken")


def default_set_next_token(
    request_kwargs: T_KWARGS,
    next_token: str,
):
    """
    Set pageToken in request parameters for next API call.
    """
    request_kwargs["pageToken"] = next_token


def paginate(
    method: T.Callable,
    items_field: str,
    page_size: int,
    max_items: int,
    kwargs: dict[str, T.Any] | None = None,
    set_page_size: T.Callable[[T_KWARGS, int], None] = default_set_page_size,
    get_next_token: T.Callable[[T_RESPONSE], str | None] = default_get_next_token,
    set_next_token: T.Callable[[T_KWARGS, str], None] = default_set_next_token,
) -> T.Iterator[dict[str, T.Any]]:
    """
    Abstract pagination function for Gmail API list methods.

    Handles the common pagination pattern used by Gmail API endpoints where
    responses contain a nextPageToken field for retrieving subsequent pages.
    Automatically manages token passing between requests and respects item limits.

    :param method: Gmail API method that returns a Resource for execution, example:
        - https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/list
        - https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.threads/list
    :param items_field: field in API response containing the list of items
    :param get_next_token: Function to extract nextPageToken from API response
    :param set_next_token: Function to set pageToken in request parameters
    :param max_items: Maximum total items to return across all pages
    :param kwargs: Initial parameters for the API call

    :yields: API response dictionaries containing paginated results

    Example:
        Using with Gmail messages list API::

            def get_token(res):
                return res.get("nextPageToken")

            def set_token(kw, token):
                kw["pageToken"] = token

            for response in _paginate(
                method=client.users().messages().list,
                items_field="messages",
                get_next_token=get_token,
                set_next_token=set_token,
                max_items=100,
                kwargs={"userId": "me"}
            ):
                print(f"Got {len(response['messages'])} messages")
    """
    items_returned = 0
    if kwargs is None:
        kwargs = {}
    set_page_size(kwargs, page_size)

    while True:
        # Execute the API call
        response = method(**kwargs).execute()
        items_in_response = len(response.get(items_field, []))
        items_returned += items_in_response

        yield response

        # Check if we've reached the maximum items limit
        if items_returned >= max_items:
            break

        # Get next page token for pagination
        next_token = get_next_token(response)
        if next_token is None:
            break  # No more pages available
        else:
            set_next_token(kwargs, next_token)
