# -*- coding: utf-8 -*-

import typing as T

try:
    from more_itertools import batched
except ImportError as e:
    from itertools import batched

if T.TYPE_CHECKING:
    from googleapiclient._apis.gmail.v1 import GmailResource


def batch_get(
    gmail: "GmailResource",
    method: T.Callable,
    ids: list[T.Any],
    id_arg_name: str,
    batch_size: int = 50,
    kwargs: dict[str, T.Any] | None = None,
):
    if kwargs is None:
        kwargs = {}

    items = list()

    def callback(
        request_id,
        response,
        exception,
    ):
        if exception is not None:
            print(f"Error for request {request_id}: {exception}")
        else:
            items.append(response)

    for sub_ids in batched(ids, batch_size):
        batch_request = gmail.new_batch_http_request()
        for id in sub_ids:
            kwargs[id_arg_name] = id
            batch_request.add(
                method(**kwargs),
                callback=callback,
            )
        batch_request.execute()

    return items
