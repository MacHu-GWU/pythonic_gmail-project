# -*- coding: utf-8 -*-

from pythonic_gmail.client import batch_get_threads
from pythonic_gmail.tests.one import one
from rich import print as rprint

ids = [
    "199599553c319566",
    "199598bcc7491337",
    "1995984aaf02e9ff",
]
threads = batch_get_threads(
    one.client,
    ids=ids,
    batch_size=2,
    kwargs={"userId": "me", "format": "minimal"},
)
for i, thread in enumerate(threads):
    print(f"===== {i} =====")
    rprint(thread)
