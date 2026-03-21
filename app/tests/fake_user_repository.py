from app.repositories.user_repository_interface import UserRepositoryInterface
from app.exceptions.repository import NotFoundError
from app.entities.user import User


class FakeUserRepository(UserRepositoryInterface):
    def __init__(self):
        self.users: dict[int, User] = {}
        self.id_count: int = 1

    def save(self, user: User):
        # trocar banco por dicionario users

        _id = user.id

        if _id == None:
            user.__id = _id
            _id = self.id_count

        
        _user = self.users.get(user.id)

        if _user:
            _user.name = user.name
            _user.email = user.email
            _user.password = user.password
            _user.blocked = user.blocked
        else:
            _user = user

        self.users.update({_user.id: _user})


    def get_by_id_or_fail(self, id: int) -> User:

        user = self.get_by_id(id)
        if not user:
            raise NotFoundError("User not found")

        return user
    
    def get_by_id(self, id) -> User | None:

        user = self.users.get(id)

        return user
        

    def list(self) -> list[User]:

        return [user for user in self.users.values()]
