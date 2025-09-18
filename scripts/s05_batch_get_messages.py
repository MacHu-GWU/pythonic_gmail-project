# -*- coding: utf-8 -*-

"""
This script demonstrates how to batch retrieve multiple Gmail messages using the Gmail API.
"""

import typing as T
from more_itertools import batched
from pythonic_gmail.tests.one import one

from settings import write, path_batch_get_messages_results

if T.TYPE_CHECKING:  # pragma: no cover
    from googleapiclient._apis.gmail.v1 import GmailResource

message_id_list = [
    "19959e8dc4ed58dc",
    "199599553c319566",
    "199598bcc7491337",
]


def batch_get_messages(
    gmail: "GmailResource",
    message_id_list: list[str],
    batch_size: int = 100,
):
    message_list = []

    # 处理回调函数
    def message_callback(
        request_id,
        response,
        exception,
    ):
        """批量请求的回调函数"""
        if exception is not None:
            print(f"Error for request {request_id}: {exception}")
        else:
            message_list.append(response)

    # 分批处理（每批最多100个）
    for sub_id_list in batched(message_id_list, batch_size):
        batch = gmail.new_batch_http_request()
        # 添加每个请求到批量中
        for message_id in sub_id_list:
            batch.add(
                gmail.users()
                .messages()
                .get(
                    userId="me",
                    id=message_id,
                    format="full",  # 获取完整邮件内容
                ),
                callback=message_callback,
            )

        # 执行批量请求
        batch.execute()

    return message_list


message_list = batch_get_messages(
    one.client,
    message_id_list=message_id_list,
    batch_size=10,
)
write(path_batch_get_messages_results, message_list)
