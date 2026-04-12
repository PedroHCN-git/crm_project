from app.services.user_service_interface import UserServiceInterface
from app.repositories.user_repository_interface import UserRepositoryInterface
from app.dto.user import UserCreateDTO, UserResponseDTO
from app.utils import handle_exceptions
from app.mappers import UserMapperProtocol
from typing import Optional

class UserService(UserServiceInterface):
    
    def __init__(self, user_repository: UserRepositoryInterface, mapper: UserMapperProtocol):
        self.user_repository = user_repository
        self.mapper = mapper

    @handle_exceptions()
    def save(self, user: UserCreateDTO):
        
        new_user = self.__transform_dto(user)

        self.user_repository.save(new_user)
    
    @handle_exceptions()
    def get_by_id(self, id: str) -> Optional[UserResponseDTO]:

        user = self.user_repository.get_by_id(int(id))

        if not user:
            return None
        
        return self.mapper.to_dto(user)
    
    @handle_exceptions()
    def list(self) -> list[UserResponseDTO]:
        users_list = self.user_repository.list()

        if not users_list:
            return []
        
        return [self.mapper.to_dto(user) for user in users_list]

    @handle_exceptions()
    def change_email(self, id: int, email: str):
        user = self.user_repository.get_by_id_or_fail(id)

        user.email = email
        
        self.user_repository.change_email(email)
    
    @handle_exceptions()
    def change_password(self, id: int, password: str):
        user = self.user_repository.get_user(id)

        user.password = password
        
        self.user_repository.update_password(user)
        
        return

    @handle_exceptions()
    def unblock(self, id):
        user = self.user_repository.get_user(id)

        user.blocked = False
    