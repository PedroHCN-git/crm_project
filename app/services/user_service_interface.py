from abc import ABC, abstractmethod
from app.dto.user import UserDTO
from typing import Optional

class UserServiceInterface(ABC):

    @abstractmethod
    def save_user(self, user: UserDTO) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_users(self) -> list[UserDTO]:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: int) -> Optional[UserDTO]:
        raise NotImplementedError
