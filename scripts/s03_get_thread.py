# -*- coding: utf-8 -*-

import pythonic_gmail.api as pg
from pythonic_gmail.tests.one import one

from settings import write, path_get_thread_result

thread_id = "19954069ab0b0270"
res = one.client.users().threads().get(userId="me", id=thread_id).execute()
write(path_get_thread_result, res)
