from app.services.user_service_interface import UserServiceInterface
from app.repositories.user_repository_interface import UserRepositoryInterface
from app.dto.user import UserDTO
from app.entities.user import User
from typing import Optional
import re

class UserService(UserServiceInterface):
    
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository


    def save_user(self, user: UserDTO) -> bool:
        
        new_user = self.__transform_dto(user)

        return self.user_repository.save_user(new_user)
    

    def get_user(self, id: int) -> Optional[UserDTO]:
        user = self.user_repository.get_user(id)

        if not user:
            return None
        
        return self.__transform_entity(user)
    

    def get_users(self) -> list[UserDTO]:
        users_list = self.user_repository.get_users()

        if not users_list:
            return []
        
        return [self.__transform_entity(user) for user in users_list]    

    
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
    