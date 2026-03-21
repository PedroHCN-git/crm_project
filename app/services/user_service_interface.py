from abc import ABC, abstractmethod
from app.dto.user import UserDTO
from typing import Optional
from app.services.base_service_interface import BaseServiceInterface

class UserServiceInterface(BaseServiceInterface[UserDTO]):
    
    @abstractmethod
    def unblock(self, id: int):
        raise NotImplementedError
    
    @abstractmethod
    def change_email(self, id: int, email: str):
        raise NotImplementedError
    
    @abstractmethod
    def change_password(self, id: int, password: str):
        raise NotImplementedError
