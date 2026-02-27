from app.repositories.user_repository_interface import UserRepositoryInterface
from app.entities.user import User
from app.infra.user_orm import UserORM
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy import select


class FakeUserRepository(UserRepositoryInterface):
    def __init__(self, engine: Engine):
        self.engine = engine
        self.session = Session(engine)

    def save_user(self, user: User):
        try:
            with self.session(self.engine) as s:
                new_user = UserORM(
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    blocked=user.blocked
                )
                s.add(new_user)
                s.commit()

                orm_to_user = User(
                    new_user.name,
                    new_user.email,
                    new_user.password,
                    new_user.blocked,
                    new_user.id
                )
            return orm_to_user
        except Exception:
            return None

    def get_user(self, id: int):
        stmt = select(User).where(User.id == id)

        print(stmt)