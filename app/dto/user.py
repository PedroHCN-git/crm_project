from pydantic import BaseModel, Field


class BaseUserDTO(BaseModel):
    name: str = Field(...)
    email: str = Field(...)


class UserCreateDTO(BaseUserDTO):
    password: str = Field(...)


class UserResponseDTO(BaseUserDTO):
    user_id: int = Field(...)
