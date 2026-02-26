from abc import ABC, abstractmethod
from app.repositories.user_repository_interface import UserRepositoryInterface


class UserServiceInterface(ABC):

    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    @abstractmethod
    def create_user(self):
        raise NotImplementedError

    @abstractmethod
    def get_users(self):
        raise NotImplementedError

    @abstractmethod
    def get_user(self, id: int):
        raise NotImplementedError
