# -*- coding: utf-8 -*-

import typing as T
from functools import cached_property

if T.TYPE_CHECKING:  # pragma: no cover
    from googleapiclient._apis.gmail.v1 import GmailResource

from .client import auth


class One:
    @cached_property
    def client(self) -> "GmailResource":
        return auth()


one = One()
