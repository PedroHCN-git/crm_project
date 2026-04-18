from pydantic import BaseModel, Field
from typing import Optional


class BaseUserDTO(BaseModel):
    name: str = Field(...)
    email: str = Field(...)


class UserCreateDTO(BaseUserDTO):
    password: str = Field(...)


class UserResponseDTO(BaseUserDTO):
    user_id: int = Field(...)
    blocked: bool = Field(...)


class UserDataActualizeDTO(BaseModel):
    name: Optional[str] = Field(default=None)
    email: Optional[str] = Field(default=None)
    password: Optional[str] = Field(default=None)
    blocked: Optional[bool] = Field(default=None)
