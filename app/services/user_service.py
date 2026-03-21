from app.services.user_service_interface import UserServiceInterface
from app.repositories.user_repository_interface import UserRepositoryInterface
from app.dto.user import UserDTO
from app.entities.user import User
from typing import Optional
from app.exceptions.domain import DomainException

class UserService(UserServiceInterface):
    
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository


    def save(self, user: UserDTO):
        
        new_user = self.__transform_dto(user)

        return self.user_repository.save(new_user)
    

    def get_by_id(self, id: int) -> Optional[UserDTO]:
        user = self.user_repository.get_by_id(id)

        if not user:
            return None
        
        return self.__transform_entity(user)
    

    def list(self) -> list[UserDTO]:
        users_list = self.user_repository.list()

        if not users_list:
            return []
        
        return [self.__transform_entity(user) for user in users_list]


    def change_email(self, id: int, email: str):
        user = self.user_repository.get_by_id_or_fail(id)

        try:
            user.email = email
        except DomainException as e:
            raise e
        
        self.user_repository.change_email(email)
    

    def change_password(self, id: int, password: str):
        user = self.user_repository.get_user(id)

        try:
            user.password = password
        except DomainException as e:
            raise e
        
        self.user_repository.update_password(user)
        
        return


    def unblock(self, id):
        user = self.user_repository.get_user(id)

        user.blocked = False
    
    def __transform_dto(self, user: UserDTO) -> User:
        new_user = User(
            user.name,
            user.email,
            user.password,
            id=user.user_id
        )

        return new_user
    
    def __transform_entity(self, user: User) -> UserDTO:
        user_dto = UserDTO(
            user.id,
            user.name,
            user.email,
            user.password
        )

        return user_dto
    
if __name__ == '__main__':
    user_service = UserService()
    