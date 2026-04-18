from abc import abstractmethod, ABC
from typing import Optional
from pydantic import BaseModel


class UserServiceInterface(ABC):
    @abstractmethod
    def save(self, dto: BaseModel):
        raise NotImplementedError

    @abstractmethod
    def list() -> list[BaseModel]:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(self, id: int) -> Optional[BaseModel]:
        raise NotImplementedError
    
    @abstractmethod
    def unblock(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def actualize_data(self, user_id: str, user_data: BaseModel):
        raise NotImplementedError
