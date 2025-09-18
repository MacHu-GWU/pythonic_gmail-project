# -*- coding: utf-8 -*-

from pythonic_gmail.client import pagi_list_messages
from pythonic_gmail.tests.one import one
from rich import print as rprint

iterproxy = pagi_list_messages(
    one.client,
    kwargs={"userId": "me"},
    page_size=2,
    max_items=6,
)

for i, res in enumerate(iterproxy):
    rprint(i, res)

for i, msg in enumerate(iterproxy.iter_items()):
    rprint(i, msg)
