from app.services.user_service_interface import UserServiceInterface
from app.repositories.user_repository_interface import UserRepositoryInterface
from app.dto.user import UserCreateDTO, UserResponseDTO, UserDataActualizeDTO
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
    def actualize_data(self, user_id: str, user_data: UserDataActualizeDTO):
        user = self.user_repository.get_by_id_or_fail(int(user_id))

        user = self.mapper.actualize_data(user_data, user)
        
        self.user_repository.save(user)


    @handle_exceptions()
    def unblock(self, id):
        user = self.user_repository.get_user(id)

        user.blocked = False
    