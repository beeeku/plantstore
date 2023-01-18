# This file was auto-generated by Fern from our API Definition.

import abc
import functools
import inspect
import logging
import typing
import uuid

import fastapi
import starlette

from ...core.abstract_fern_service import AbstractFernService
from ...core.exceptions.fern_http_exception import FernHTTPException
from ...core.route_args import get_route_args
from ...security import ApiAuth, FernAuth
from .errors.invalid_id_supplied_error import InvalidIdSuppliedError
from .errors.invalid_response_error import InvalidResponseError
from .errors.plant_not_found_error import PlantNotFoundError
from .types.add_plant_request import AddPlantRequest
from .types.plant import Plant


class AbstractPlantService(AbstractFernService):
    """
    AbstractPlantService is an abstract class containing the methods that your
    PlantService implementation should implement.

    Each method is associated with an API route, which will be registered
    with FastAPI when you register your implementation using Fern's register()
    function.
    """

    @abc.abstractmethod
    def add(self, *, body: AddPlantRequest, auth: ApiAuth) -> None:
        """
        Add a new plant to the store.
        """
        ...

    @abc.abstractmethod
    def find(self, *, plant_id: uuid.UUID, auth: ApiAuth) -> Plant:
        ...

    @abc.abstractmethod
    def delete(self, *, plant_id: uuid.UUID, auth: ApiAuth) -> None:
        ...

    """
    Below are internal methods used by Fern to register your implementation.
    You can ignore them.
    """

    @classmethod
    def _init_fern(cls, router: fastapi.APIRouter) -> None:
        cls.__init_add(router=router)
        cls.__init_find(router=router)
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
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> None:
            try:
                return cls.add(*args, **kwargs)
            except InvalidResponseError as e:
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
            path="/plant",
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=cls.add.__doc__,
            **get_route_args(cls.add, default_tag="plant"),
        )(wrapper)

    @classmethod
    def __init_find(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.find)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "plant_id":
                new_parameters.append(parameter.replace(default=fastapi.Path(...)))
            elif parameter_name == "auth":
                new_parameters.append(parameter.replace(default=fastapi.Depends(FernAuth)))
            else:
                new_parameters.append(parameter)
        setattr(cls.find, "__signature__", endpoint_function.replace(parameters=new_parameters))

        @functools.wraps(cls.find)
        def wrapper(*args: typing.Any, **kwargs: typing.Any) -> Plant:
            try:
                return cls.find(*args, **kwargs)
            except (PlantNotFoundError, InvalidIdSuppliedError) as e:
                raise e
            except FernHTTPException as e:
                logging.getLogger(f"{cls.__module__}.{cls.__name__}").warn(
                    f"Endpoint 'find' unexpectedly threw {e.__class__.__name__}. "
                    + f"If this was intentional, please add {e.__class__.__name__} to "
                    + "the endpoint's errors list in your Fern Definition."
                )
                raise e

        # this is necessary for FastAPI to find forward-ref'ed type hints.
        # https://github.com/tiangolo/fastapi/pull/5077
        wrapper.__globals__.update(cls.find.__globals__)

        router.get(
            path="/plant/{plant_id}",
            response_model=Plant,
            description=cls.find.__doc__,
            **get_route_args(cls.find, default_tag="plant"),
        )(wrapper)

    @classmethod
    def __init_delete(cls, router: fastapi.APIRouter) -> None:
        endpoint_function = inspect.signature(cls.delete)
        new_parameters: typing.List[inspect.Parameter] = []
        for index, (parameter_name, parameter) in enumerate(endpoint_function.parameters.items()):
            if index == 0:
                new_parameters.append(parameter.replace(default=fastapi.Depends(cls)))
            elif parameter_name == "plant_id":
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
            except (PlantNotFoundError, InvalidIdSuppliedError) as e:
                raise e
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
            path="/plant/{plant_id}",
            status_code=starlette.status.HTTP_204_NO_CONTENT,
            description=cls.delete.__doc__,
            **get_route_args(cls.delete, default_tag="plant"),
        )(wrapper)
