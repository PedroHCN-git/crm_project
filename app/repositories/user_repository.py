from app.repositories.user_repository_interface import UserRepositoryInterface
from app.exceptions.repository import NotFoundError
from app.entities.user import User
from app.infra.user_orm import UserORM
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy import select

class UserRepository(UserRepositoryInterface):
    def __init__(self, engine: Engine):
        self.engine = engine
        self.session = Session(engine)

    def save(self, user: User):
        try:
            with self.session as s:
                new_user = UserORM(
                    name=user.name,
                    email=user.email,
                    password=user.password,
                    blocked=user.blocked
                )
                s.add(new_user)
                s.commit()
        except Exception:
            return False

        return True
    

    def get_by_id_or_fail(self, id: int):

        user = self.get_by_id(id)
        if not user:
            raise NotFoundError("User not found")

        return user
    
    def get_by_id(self, id):
        stmt = select(UserORM).where(UserORM.id == id)
        results = self.session.scalars(stmt)

        user = None
        user_data = None

        for result in results:
            user_data = result

        if user_data:
            user = User(
                user_data.name,
                user_data.email,
                user_data.password,
                user_data.blocked,
                user_data.id
            )

        return user
        

    def list(self):
        stmt = select(UserORM)
        results = self.session.scalars(stmt)

        user_list = []
        user_data = None

        for result in results:
            user_data = result

            if user_data:
                user = User(
                    user_data.name,
                    user_data.email,
                    user_data.password,
                    user_data.blocked,
                    user_data.id
                )

                user_list.append(user)

        return user_list