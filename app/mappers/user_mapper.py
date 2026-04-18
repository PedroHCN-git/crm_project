from app.dto.user import UserCreateDTO, UserResponseDTO, UserDataActualizeDTO
from app.entities.user import User
from typing import Protocol

class UserMapperProtocol(Protocol):
    def to_entity(dto: UserCreateDTO) -> User: ...
    def to_dto(entity: User) -> UserResponseDTO: ...
    def actualize_data(dto: UserDataActualizeDTO, entity: User) -> User: ...

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
            user_id=entity.id,
            blocked=entity.blocked
        )
    
    @staticmethod
    def actualize_data(dto: UserDataActualizeDTO, entity: User) -> User:
        if dto.name is not None:
            entity.name = dto.name
        
        if dto.email is not None:
            entity.email = dto.email

        if dto.password is not None:
            entity.password = dto.password

        return entity