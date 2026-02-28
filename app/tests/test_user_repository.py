from app.tests.fake_user_repository import FakeUserRepository
from app.entities.user import User
from sqlalchemy import create_engine

# testar apenas listagem e salvamento de dados, verificação de dados é regra de negócio
# responsabilidade do service

engine = create_engine('sqlite:///crm_database.db')

user1 = User(
    "giovana corradini",
    "giovana@gmail.com.br",
    "123",
    False
)

user2 = User(
    "pedro corradini",
    "teste@gmail.com",
    "123",
    False
)

user3 = User(
    "patricia corradini",
    "patrcia@gmail.com",
    "457",
    True
)

user4 = User(
    "leandro nunes",
    "leandro@gmail.com",
    "908",
    True
)

user5 = User(
    "jessica corradini",
    "jessica@gmail.com",
    "873",
    False
)

user_list = [user1, user2, user3, user4, user5]

def test_get_users():
    repository = FakeUserRepository(engine)

    _user_list = repository.get_users()

    for i, user in enumerate(_user_list):
        assert str(user) == str(user_list[i])
