from app.repositories.base_repository_interface import BaseRepositoryInterface
from app.entities.user import User


class UserRepositoryInterface(BaseRepositoryInterface[User]):
    pass
