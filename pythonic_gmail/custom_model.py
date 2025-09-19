# -*- coding: utf-8 -*-

import dataclasses

from func_args.api import REQ, OPT, BaseFrozenModel


@dataclasses.dataclass(frozen=True)
class Email(BaseFrozenModel):
    email: str = dataclasses.field(default=REQ)
    name: str | None = dataclasses.field(default=None)

    @property
    def full_name(self) -> str:
        if self.name:
            return f"{self.name} <{self.email}>"
        else:
            return self.email
