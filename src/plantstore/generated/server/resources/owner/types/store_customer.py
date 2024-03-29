# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic
import typing_extensions

from ...plant.types.plant import Plant
from .owner_id import OwnerId


class StoreCustomer(pydantic.BaseModel):
    name: str
    age: typing.Optional[int]
    plants: typing.List[Plant]
    lifetime_spend: float
    id: OwnerId

    class Partial(typing_extensions.TypedDict):
        name: typing_extensions.NotRequired[str]
        age: typing_extensions.NotRequired[typing.Optional[int]]
        plants: typing_extensions.NotRequired[typing.List[Plant]]
        lifetime_spend: typing_extensions.NotRequired[float]
        id: typing_extensions.NotRequired[OwnerId]

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid
