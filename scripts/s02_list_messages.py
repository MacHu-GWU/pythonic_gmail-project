# -*- coding: utf-8 -*-

"""
**重要结论**

经过调研, 你无法使用 list API 获得除了 id 和 threadId 之外的任何信息.
你必须之后自己用 batch get API 获得 details
"""

import pythonic_gmail.api as pg
from pythonic_gmail.tests.one import one

from settings import write, path_list_messages_results

res = one.client.users().messages().list(userId="me").execute()
write(path_list_messages_results, res)
