# -*- coding: utf-8 -*-

from functools import cached_property

from .client import auth


class One:
    @cached_property
    def client(self):
        return auth()

one = One()
