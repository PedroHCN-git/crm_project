from abc import ABC, abstractmethod
from app.infra.user_orm import UserORM

class UserRepositoryInterface(ABC):
    def __init__(self, user_orm: UserORM):
        pass