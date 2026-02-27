from app.utils.password import valid_password
from typing import Optional


class User():
    def __init__(
        self,
        name: str,
        email: str,
        password: str,
        blocked: bool,
        id: Optional[int] = None
    ):
        self.__id = id
        self.__name = name
        self.__email = email
        self.__password = password
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
            raise Exception("user is blocked, can't change hes name")

        self.__name = new_user_name

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, new_user_email: str):
        if self.__blocked:
            raise Exception("user is blocked, can't change his e-mail")

        self.__email == new_user_email

    @property
    def password(self):
        return self.__password

    @property
    def blocked(self):
        return self.__blocked

    def user_unblock(self):
        self.__blocked = False

    def change_user_password(self, new_password: str):
        if self.__blocked:
            raise Exception("user is blocked, can't change his password")

        if not valid_password(new_password):
            raise Exception("new password is not valid, please follow the pattern stablished")

        self.__password = new_password

    def __str__(self):
        return f'{self.id, self.name, self.email}'
