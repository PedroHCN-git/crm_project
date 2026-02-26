from abc import ABC, abstractmethod
from app.entities.user import User


class UserRepositoryInterface(ABC):
    def __init__(self, user: User):
        pass

        @abstractmethod
        def save_user(self):
            raise NotImplementedError

        @abstractmethod
        def get_user(self, id: int):
            raise NotImplementedError

        @abstractmethod
        def get_users(self, id: int):
            raise NotImplementedError
