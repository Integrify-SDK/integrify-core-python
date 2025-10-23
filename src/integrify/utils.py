from enum import Enum
from typing import Annotated, Literal, TypeVar, Union

from pydantic import BaseModel, Field

_ResponseT = TypeVar('_ResponseT', bound=Union[BaseModel, dict])
"""Dynamic response type."""

T = TypeVar('T')


class UnsetType:
    """Sentinel type to indicate an unset field value."""

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __repr__(self):
        return 'UNSET'

    def __str__(self):
        return 'UNSET'

    def __bool__(self):
        return False


UNSET = UnsetType()
"""Set olunmamış argument dəyəri"""

Unset = Union[T, Literal[UNSET]]  # type: ignore[valid-type]
""" Optional argument tipi """

UnsettOrNone = Union[T, Literal[UNSET], None]  # type: ignore[valid-type]
"""None dəyəri ala bilən optional argument tipi"""

UnsetField = Annotated[Unset[T], Field(default=UNSET)]
"""Pydantic üçün set olunmamış argument dəyəri"""

UnsetOrNoneField = Annotated[UnsettOrNone[T], Field(default=UNSET)]
"""Pydantic üçün set olunmamış və None dəyəri ala bilən argument dəyəri"""


class Environment(str, Enum):
    TEST = 'test'
    PROD = 'prod'
