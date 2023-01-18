# This file was auto-generated by Fern from our API Definition.

import typing

import pydantic

from ...plant.types.plant import Plant
from ..types.owner_age import OwnerAge


class AddOwnerRequest(pydantic.BaseModel):
    name: str
    age: OwnerAge
    plants: typing.List[Plant]

    class Config:
        frozen = True
