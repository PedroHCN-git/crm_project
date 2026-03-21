from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')
class BaseServiceInterface(ABC, Generic[T]):

    @abstractmethod
    def save(self, dto: T):
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError