from app.dto.user import UserCreateDTO, UserResponseDTO
from app.entities.user import User
from typing import Protocol

class UserMapperProtocol(Protocol):
    def to_entity(dto: UserCreateDTO) -> User: ...
    def to_dto(entity: User) -> UserResponseDTO: ...

class UserMapper(UserMapperProtocol):

    @staticmethod
    def to_entity(dto: UserCreateDTO) -> User:
        return User(
            dto.name,
            dto.email,
            dto.password
        )
    
    @staticmethod
    def to_dto(entity: User) -> UserResponseDTO:
        return UserResponseDTO(
            name=entity.name,
            email=entity.email,
            user_id=entity.id
        )