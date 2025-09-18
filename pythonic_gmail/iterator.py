# -*- coding: utf-8 -*-

import typing as T

from iterproxy import IterProxy

from .model import (
    T_BASE,
    Message,
    ListMessagesResponse,
    Thread,
    ListThreadsResponse,
)


class BaseIterProxy(IterProxy):
    @classmethod
    def from_paginator(
        cls,
        paginator: T.Iterable,
        klass: T.Type[T_BASE],
    ):
        return cls(
            (klass.new(res) for res in paginator),
        )


class ListMessagesResponseIterProxy(BaseIterProxy["ListMessagesResponse"]):
    def iter_items(self):
        res: "ListMessagesResponse"
        message: "Message"
        for res in self:
            for message in res.messages:
                yield message


class ListThreadsResponseIterProxy(BaseIterProxy["ListThreadsResponse"]):
    def iter_items(self):
        res: "ListThreadsResponse"
        thread: "Thread"
        for res in self:
            for thread in res.threads:
                yield thread
