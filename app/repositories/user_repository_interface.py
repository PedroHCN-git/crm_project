from app.repositories.base_repository_interface import BaseRepositoryInterface
from app.entities.user import User
from abc import abstractmethod


class UserRepositoryInterface(BaseRepositoryInterface[User]):
    pass