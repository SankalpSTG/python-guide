from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel

T = TypeVar("T")

class ResponseType(GenericModel, Generic[T]):
  status: int
  message: str
  data: Optional[T] = None