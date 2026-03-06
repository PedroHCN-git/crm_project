from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar

T = TypeVar('T')
class BaseRepositoryInterface(ABC, Generic[T]):

    @abstractmethod
    def save(self, obj: T):
        raise NotImplementedError
    
    @abstractmethod
    def update(self, id: int):
        raise NotImplementedError

    @abstractmethod
    def list(self) -> list[T]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[T]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id_or_fail(self, id: int) -> T:
        raise NotImplementedError