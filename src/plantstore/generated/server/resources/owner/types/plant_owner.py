# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .store_customer import StoreCustomer
from .store_employee import StoreEmployee

T_Result = typing.TypeVar("T_Result")


class _Factory:
    def customer(self, value: StoreCustomer) -> PlantOwner:
        return PlantOwner(__root__=_PlantOwner.Customer(**dict(value), type="customer"))

    def employee(self, value: StoreEmployee) -> PlantOwner:
        return PlantOwner(__root__=_PlantOwner.Employee(**dict(value), type="employee"))


class PlantOwner(pydantic.BaseModel):
    factory: typing.ClassVar[_Factory] = _Factory()

    def get_as_union(self) -> typing.Union[_PlantOwner.Customer, _PlantOwner.Employee]:
        return self.__root__

    def visit(
        self, customer: typing.Callable[[StoreCustomer], T_Result], employee: typing.Callable[[StoreEmployee], T_Result]
    ) -> T_Result:
        if self.__root__.type == "customer":
            return customer(self.__root__)
        if self.__root__.type == "employee":
            return employee(self.__root__)

    __root__: typing_extensions.Annotated[
        typing.Union[_PlantOwner.Customer, _PlantOwner.Employee], pydantic.Field(discriminator="type")
    ]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @PlantOwner.Validators.validate
            def validate(value: typing.Union[_PlantOwner.Customer, _PlantOwner.Employee]) -> typing.Union[_PlantOwner.Customer, _PlantOwner.Employee]:
                ...
        """

        _validators: typing.ClassVar[
            typing.List[
                typing.Callable[
                    [typing.Union[_PlantOwner.Customer, _PlantOwner.Employee]],
                    typing.Union[_PlantOwner.Customer, _PlantOwner.Employee],
                ]
            ]
        ] = []

        @classmethod
        def validate(
            cls,
            validator: typing.Callable[
                [typing.Union[_PlantOwner.Customer, _PlantOwner.Employee]],
                typing.Union[_PlantOwner.Customer, _PlantOwner.Employee],
            ],
        ) -> None:
            cls._validators.append(validator)

    @pydantic.root_validator(pre=False)
    def _validate(cls, values: typing.Dict[str, typing.Any]) -> typing.Dict[str, typing.Any]:
        value = typing.cast(typing.Union[_PlantOwner.Customer, _PlantOwner.Employee], values.get("__root__"))
        for validator in PlantOwner.Validators._validators:
            value = validator(value)
        return {**values, "__root__": value}

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        extra = pydantic.Extra.forbid


class _PlantOwner:
    class Customer(StoreCustomer):
        type: typing_extensions.Literal["customer"]

        class Config:
            frozen = True

    class Employee(StoreEmployee):
        type: typing_extensions.Literal["employee"]

        class Config:
            frozen = True


PlantOwner.update_forward_refs()