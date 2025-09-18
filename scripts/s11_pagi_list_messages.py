# -*- coding: utf-8 -*-

from pythonic_gmail.client import pagi_list_messages
from pythonic_gmail.tests.one import one
from rich import print as rprint


def run():
    return pagi_list_messages(
        one.client,
        kwargs={"userId": "me"},
        page_size=2,
        max_items=6,
    )


iterproxy = run()
for i, res in enumerate(iterproxy):
    # print(res.messages)
    rprint(i, res)

iterproxy = run()
for i, msg in enumerate(iterproxy.iter_items()):
    # print(msg.id)
    rprint(i, msg)
