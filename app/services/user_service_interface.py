from abc import ABC, abstractmethod
from app.dto.user import UserDTO
from typing import Optional

class UserServiceInterface(ABC):

    @abstractmethod
    def save_user(self, user: UserDTO):
        raise NotImplementedError

    @abstractmethod
    def get_users(self) -> list[UserDTO]:
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: int) -> Optional[UserDTO]:
        raise NotImplementedError
    
    @abstractmethod
    def unblock_user(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def change_email(self, id: int, email: str):
        raise NotImplementedError
    
    @abstractmethod
    def change_password(self, id: int, password: str):
        raise NotImplementedError
