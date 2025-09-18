# -*- coding: utf-8 -*-

from pythonic_gmail.client import batch_get_messages
from pythonic_gmail.tests.one import one
from rich import print as rprint

ids = [
    "19959e8dc4ed58dc",
    "199599553c319566",
    "199598bcc7491337",
]
messages = batch_get_messages(
    one.client,
    ids=ids,
    batch_size=2,
    kwargs={"userId": "me", "format": "minimal"},
)
for i, msg in enumerate(messages):
    print(f"===== {i} =====")
    rprint(msg)
