# -*- coding: utf-8 -*-

import dataclasses

from func_args.api import REQ

from .base import Base


@dataclasses.dataclass(frozen=True)
class User(Base):
    """ """

    _data: dict = dataclasses.field(default=REQ)
