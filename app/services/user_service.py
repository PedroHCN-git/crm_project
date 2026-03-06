from app.services.user_service_interface import UserServiceInterface
from app.repositories.user_repository_interface import UserRepositoryInterface
from app.dto.user import UserDTO
from app.entities.user import User
from typing import Optional
from app.exceptions.domain import DomainException
from app.exceptions.service import UserNotFoundException

class UserService(UserServiceInterface):
    
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository


    def save_user(self, user: UserDTO) -> bool:
        
        new_user = self.__transform_dto(user)

        return self.user_repository.save_user(new_user)
    

    def get_user(self, id: int) -> Optional[UserDTO]:
        user = self.user_repository.get_user(id)

        if not user:
            raise UserNotFoundException("User not found")
        
        return self.__transform_entity(user)
    

    def get_users(self) -> list[UserDTO]:
        users_list = self.user_repository.get_users()

        if not users_list:
            return []
        
        return [self.__transform_entity(user) for user in users_list]


    def change_email(self, id: int, email: str):
        user = self.user_repository.get_user(id)

        if not user:
            raise UserNotFoundException("User not found")

        try:
            user.email = email
        except DomainException as e:
            raise e
        
        return
    

    def change_password(self, id: int, password: str):
        user = self.user_repository.get_user(id)

        if not user:
            raise UserNotFoundException("User not found")

        try:
            user.password = password
        except DomainException as e:
            raise e
        
        self.user_repository.update_password(user)
        
        return


    def unblock_user(self, id):
        user = self.user_repository.get_user(id)

        user.blocked = False
    
    def __transform_dto(self, user: UserDTO) -> User:
        new_user = User(
            user.name,
            user.email,
            user.password
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
    