from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')
class BaseRepositoryInterface(ABC, Generic[T]):

    @abstractmethod
    def save(self, obj: T):
        raise NotImplementedError

    def list(self) -> list[T]:
        raise NotImplementedError

    def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError

    def get_by_id_or_fail(self, id: int) -> T:
        raise NotImplementedError