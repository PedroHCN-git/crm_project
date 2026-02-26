from abc import ABC, abstractmethod
from app.entities.user import User
from typing import Optional


class UserRepositoryInterface(ABC):

    @abstractmethod
    def create_user() -> User:
        raise NotImplementedError

    @abstractmethod
    def get_user(id: int) -> Optional[User]:
        raise NotImplementedError

    @abstractmethod
    def get_users() -> list[User]:
        raise NotImplementedError
