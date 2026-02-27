from fake_user_repository import FakeUserRepository
from app.entities.user import User
import json

user_data: dict = json.loads('\\user_data.json')
user_list: list[User] = [value for _, value in user_data.items()]


def test_save_user():
    repository = FakeUserRepository()

    for user in user_list:
        assert repository.save_user(user) == str(user)
