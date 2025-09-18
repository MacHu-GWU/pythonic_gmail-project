# -*- coding: utf-8 -*-

from pythonic_gmail.client import pagi_list_threads
from pythonic_gmail.tests.one import one
from rich import print as rprint


def run():
    return pagi_list_threads(
        one.client,
        kwargs={"userId": "me"},
        page_size=2,
        max_items=6,
    )


iterproxy = run()
for i, res in enumerate(iterproxy):
    # print(res.threads)
    rprint(i, res)

iterproxy = run()
for i, thread in enumerate(iterproxy.iter_items()):
    # print(thread.id)
    rprint(i, thread)
