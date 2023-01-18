# This file was auto-generated by Fern from our API Definition.

from __future__ import annotations

import typing

import pydantic
import typing_extensions

from .plant_category import PlantCategory
from .plant_id import PlantId
from .plant_status import PlantStatus


class Plant(pydantic.BaseModel):
    id: typing.Optional[PlantId]
    category: typing.Optional[PlantCategory]
    name: str
    photo_urls: typing.Dict[str, str] = pydantic.Field(alias="photoUrls")
    status: typing.Optional[PlantStatus]

    class Partial(typing_extensions.TypedDict):
        id: typing_extensions.NotRequired[typing.Optional[PlantId]]
        category: typing_extensions.NotRequired[typing.Optional[PlantCategory]]
        name: typing_extensions.NotRequired[str]
        photo_urls: typing_extensions.NotRequired[typing.Dict[str, str]]
        status: typing_extensions.NotRequired[typing.Optional[PlantStatus]]

    class Validators:
        """
        Use this class to add validators to the Pydantic model.

            @Plant.Validators.root()
            def validate(values: Plant.Partial) -> Plant.Partial:
                ...

            @Plant.Validators.field("id")
            def validate_id(id: typing.Optional[PlantId], values: Plant.Partial) -> typing.Optional[PlantId]:
                ...

            @Plant.Validators.field("category")
            def validate_category(category: typing.Optional[PlantCategory], values: Plant.Partial) -> typing.Optional[PlantCategory]:
                ...

            @Plant.Validators.field("name")
            def validate_name(name: str, values: Plant.Partial) -> str:
                ...

            @Plant.Validators.field("photo_urls")
            def validate_photo_urls(photo_urls: typing.Dict[str, str], values: Plant.Partial) -> typing.Dict[str, str]:
                ...

            @Plant.Validators.field("status")
            def validate_status(status: typing.Optional[PlantStatus], values: Plant.Partial) -> typing.Optional[PlantStatus]:
                ...
        """

        _pre_validators: typing.ClassVar[typing.List[Plant.Validators._PreRootValidator]] = []
        _post_validators: typing.ClassVar[typing.List[Plant.Validators._RootValidator]] = []
        _id_pre_validators: typing.ClassVar[typing.List[Plant.Validators.PreIdValidator]] = []
        _id_post_validators: typing.ClassVar[typing.List[Plant.Validators.IdValidator]] = []
        _category_pre_validators: typing.ClassVar[typing.List[Plant.Validators.PreCategoryValidator]] = []
        _category_post_validators: typing.ClassVar[typing.List[Plant.Validators.CategoryValidator]] = []
        _name_pre_validators: typing.ClassVar[typing.List[Plant.Validators.PreNameValidator]] = []
        _name_post_validators: typing.ClassVar[typing.List[Plant.Validators.NameValidator]] = []
        _photo_urls_pre_validators: typing.ClassVar[typing.List[Plant.Validators.PrePhotoUrlsValidator]] = []
        _photo_urls_post_validators: typing.ClassVar[typing.List[Plant.Validators.PhotoUrlsValidator]] = []
        _status_pre_validators: typing.ClassVar[typing.List[Plant.Validators.PreStatusValidator]] = []
        _status_post_validators: typing.ClassVar[typing.List[Plant.Validators.StatusValidator]] = []

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Plant.Validators._RootValidator], Plant.Validators._RootValidator]:
            ...

        @typing.overload
        @classmethod
        def root(
            cls, *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Plant.Validators._PreRootValidator], Plant.Validators._PreRootValidator]:
            ...

        @classmethod
        def root(cls, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if pre:
                    cls._pre_validators.append(validator)
                else:
                    cls._post_validators.append(validator)
                return validator

            return decorator

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Plant.Validators.PreIdValidator], Plant.Validators.PreIdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["id"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Plant.Validators.IdValidator], Plant.Validators.IdValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["category"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Plant.Validators.PreCategoryValidator], Plant.Validators.PreCategoryValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["category"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Plant.Validators.CategoryValidator], Plant.Validators.CategoryValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Plant.Validators.PreNameValidator], Plant.Validators.PreNameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["name"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Plant.Validators.NameValidator], Plant.Validators.NameValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["photo_urls"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Plant.Validators.PrePhotoUrlsValidator], Plant.Validators.PrePhotoUrlsValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["photo_urls"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Plant.Validators.PhotoUrlsValidator], Plant.Validators.PhotoUrlsValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[True]
        ) -> typing.Callable[[Plant.Validators.PreStatusValidator], Plant.Validators.PreStatusValidator]:
            ...

        @typing.overload
        @classmethod
        def field(
            cls, field_name: typing_extensions.Literal["status"], *, pre: typing_extensions.Literal[False] = False
        ) -> typing.Callable[[Plant.Validators.StatusValidator], Plant.Validators.StatusValidator]:
            ...

        @classmethod
        def field(cls, field_name: str, *, pre: bool = False) -> typing.Any:
            def decorator(validator: typing.Any) -> typing.Any:
                if field_name == "id":
                    if pre:
                        cls._id_pre_validators.append(validator)
                    else:
                        cls._id_post_validators.append(validator)
                if field_name == "category":
                    if pre:
                        cls._category_pre_validators.append(validator)
                    else:
                        cls._category_post_validators.append(validator)
                if field_name == "name":
                    if pre:
                        cls._name_pre_validators.append(validator)
                    else:
                        cls._name_post_validators.append(validator)
                if field_name == "photo_urls":
                    if pre:
                        cls._photo_urls_pre_validators.append(validator)
                    else:
                        cls._photo_urls_post_validators.append(validator)
                if field_name == "status":
                    if pre:
                        cls._status_pre_validators.append(validator)
                    else:
                        cls._status_post_validators.append(validator)
                return validator

            return decorator

        class PreIdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Plant.Partial) -> typing.Any:
                ...

        class IdValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Optional[PlantId], __values: Plant.Partial) -> typing.Optional[PlantId]:
                ...

        class PreCategoryValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Plant.Partial) -> typing.Any:
                ...

        class CategoryValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[PlantCategory], __values: Plant.Partial
            ) -> typing.Optional[PlantCategory]:
                ...

        class PreNameValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Plant.Partial) -> typing.Any:
                ...

        class NameValidator(typing_extensions.Protocol):
            def __call__(self, __v: str, __values: Plant.Partial) -> str:
                ...

        class PrePhotoUrlsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Plant.Partial) -> typing.Any:
                ...

        class PhotoUrlsValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Dict[str, str], __values: Plant.Partial) -> typing.Dict[str, str]:
                ...

        class PreStatusValidator(typing_extensions.Protocol):
            def __call__(self, __v: typing.Any, __values: Plant.Partial) -> typing.Any:
                ...

        class StatusValidator(typing_extensions.Protocol):
            def __call__(
                self, __v: typing.Optional[PlantStatus], __values: Plant.Partial
            ) -> typing.Optional[PlantStatus]:
                ...

        class _PreRootValidator(typing_extensions.Protocol):
            def __call__(self, __values: typing.Any) -> typing.Any:
                ...

        class _RootValidator(typing_extensions.Protocol):
            def __call__(self, __values: Plant.Partial) -> Plant.Partial:
                ...

    @pydantic.root_validator(pre=True)
    def _pre_validate(cls, values: Plant.Partial) -> Plant.Partial:
        for validator in Plant.Validators._pre_validators:
            values = validator(values)
        return values

    @pydantic.root_validator(pre=False)
    def _post_validate(cls, values: Plant.Partial) -> Plant.Partial:
        for validator in Plant.Validators._post_validators:
            values = validator(values)
        return values

    @pydantic.validator("id", pre=True)
    def _pre_validate_id(cls, v: typing.Optional[PlantId], values: Plant.Partial) -> typing.Optional[PlantId]:
        for validator in Plant.Validators._id_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("id", pre=False)
    def _post_validate_id(cls, v: typing.Optional[PlantId], values: Plant.Partial) -> typing.Optional[PlantId]:
        for validator in Plant.Validators._id_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("category", pre=True)
    def _pre_validate_category(
        cls, v: typing.Optional[PlantCategory], values: Plant.Partial
    ) -> typing.Optional[PlantCategory]:
        for validator in Plant.Validators._category_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("category", pre=False)
    def _post_validate_category(
        cls, v: typing.Optional[PlantCategory], values: Plant.Partial
    ) -> typing.Optional[PlantCategory]:
        for validator in Plant.Validators._category_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=True)
    def _pre_validate_name(cls, v: str, values: Plant.Partial) -> str:
        for validator in Plant.Validators._name_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("name", pre=False)
    def _post_validate_name(cls, v: str, values: Plant.Partial) -> str:
        for validator in Plant.Validators._name_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("photo_urls", pre=True)
    def _pre_validate_photo_urls(cls, v: typing.Dict[str, str], values: Plant.Partial) -> typing.Dict[str, str]:
        for validator in Plant.Validators._photo_urls_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("photo_urls", pre=False)
    def _post_validate_photo_urls(cls, v: typing.Dict[str, str], values: Plant.Partial) -> typing.Dict[str, str]:
        for validator in Plant.Validators._photo_urls_post_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=True)
    def _pre_validate_status(
        cls, v: typing.Optional[PlantStatus], values: Plant.Partial
    ) -> typing.Optional[PlantStatus]:
        for validator in Plant.Validators._status_pre_validators:
            v = validator(v, values)
        return v

    @pydantic.validator("status", pre=False)
    def _post_validate_status(
        cls, v: typing.Optional[PlantStatus], values: Plant.Partial
    ) -> typing.Optional[PlantStatus]:
        for validator in Plant.Validators._status_post_validators:
            v = validator(v, values)
        return v

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        allow_population_by_field_name = True
        extra = pydantic.Extra.forbid
