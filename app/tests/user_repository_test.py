from app.repositories.user_repository_interface import UserRepositoryInterface
from app.entities.user import User
from app.infra.user_orm import UserORM
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy import select


class UserRepositoryTeste(UserRepositoryInterface):
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
            return user
        except Exception:
            return None

    def get_user(self, id: int):
        stmt = select(User).where(User.id == id)

        print(stmt)
