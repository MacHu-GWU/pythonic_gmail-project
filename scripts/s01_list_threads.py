# -*- coding: utf-8 -*-

import typing as T

import pythonic_gmail.api as pg
from pythonic_gmail.tests.one import one

from settings import write, path_list_threads_results

res = one.client.users().threads().list(userId="me").execute()
write(path_list_threads_results, res)
