# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing
import uuid

import fastapi
import starlette

from ....core.abstract_fern_service import AbstractFernService
from ....core.exceptions.fern_http_exception import FernHTTPException
from ....core.route_args import get_route_args
from ....security import ApiAuth, FernAuth
from ..errors.owner_not_found_error import OwnerNotFoundError
from ..types.plant_owner import PlantOwner
from .add_owner_request import AddOwnerRequest


class AbstractOwnerService(AbstractFernService):
    """
    AbstractOwnerService is an abstract class containing the methods that your
    OwnerService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def add(self, *, body: AddOwnerRequest, auth: ApiAuth) -> PlantOwner:
        """
        Add a new owner as a customer of the store.
        """
        ...

    @abc.abstractmethod
    def delete(self, *, owner_id: uuid.UUID, auth: ApiAuth) -> None:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_add(router=router)
        cls.__init_delete(router=router)

    @classmethod
    def __init_add(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.add)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "body":
                new_parameters.append(parameter.replace(default=fastapi.Body(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.add, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.add)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> PlantOwner:
            try:
                return cls.add(*args, **kwargs)
            except OwnerNotFoundError as e:
                raise e
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'add' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.add.__globals__)

        router.post(
            path="/owner",
            response_model=PlantOwner,
            description=cls.add.__doc__,
            **get_route_args(cls.add, default_tag="owner"),
        )(wrapper)

    @classmethod
    def __init_delete(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.delete)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "owner_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.delete, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.delete)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.delete(*args, **kwargs)
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'delete' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.delete.__globals__)

        router.delete(
            path="/owner/{owner_id}",
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=cls.delete.__doc__,
            **get_route_args(cls.delete, default_tag="owner"),
        )(wrapper)
