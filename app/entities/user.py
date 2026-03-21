from typing import Optional
from app.exceptions.domain import (
    EmailNotValidException,
    PasswordNotValidException,
    UserBlockedException
) 
import re


class User():
    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        blocked: bool = False,
        id: Optional[int] = None
    ):
        self.__id = id
        self.__name = name
        self.__email = self.__valid_email(email)
        self.__password = self.__valid_password(password)
        self.__blocked = blocked

    # getters and setters
    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_user_name: str):
        if self.__blocked:
            raise UserBlockedException("user is blocked, can't change his name")

        self.__name = new_user_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_user_email: str):
        if self.__blocked:
            raise UserBlockedException("user is blocked, can't change his e-mail")
        
        self.__valid_email(new_user_email)
           
        self.__email == new_user_email

    @property
    def password(self):
        return self.__password

    @property
    def blocked(self):
        return self.__blocked
    
    @password.setter
    def password(self, new_user_password: str):
        if self.__blocked:
            raise UserBlockedException("user is blocked, can't change his password")

        self.__valid_password(new_user_password)

        self.__password = new_user_password


    def __valid_email(self, email: str):

        if not re.fullmatch(r'^[A-Za-z0-9._%-]+@[A-Za-z.-]+\.[A-Za-z.]{2,}', email):
            raise EmailNotValidException("User e-mail is not valid")
        
        return email


    def __valid_password(self, password: str):

        if not re.fullmatch(r'[A-Za-z0-9@#!&$%+^]{8,}', password):
            raise PasswordNotValidException("User password is not valid")
        
        return password

    def __str__(self):
        return f'{self.name, self.email}'
    
if __name__ == '__main__':
    user = User(
        'pedro',
        'pedro@gmail.com',
        'Phn142536@',
        False
    )
