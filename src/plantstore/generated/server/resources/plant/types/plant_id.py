# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing
import uuid

import pydantic


class PlantId(pydantic.BaseModel):
    __root__: uuid.UUID

    def get_as_uuid(self) -> uuid.UUID:
        return self.__root__

    @staticmethod
    def from_uuid(value: uuid.UUID) -> PlantId:
        return PlantId(__root__=value)

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
