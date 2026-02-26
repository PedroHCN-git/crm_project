from app.repositories.user_repository_interface import UserRepositoryInterface
from app.entities.user import User


class UserRepositoryTeste(UserRepositoryInterface):
    def __init__(self, user: User):
        super().__init__(user)
