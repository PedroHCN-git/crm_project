from app.repositories.user_repository_interface import UserRepositoryInterface
from app.exceptions.repository import NotFoundError
from app.entities.user import User
from app.infra.user_orm import UserORM
from sqlalchemy import Engine
from sqlalchemy.orm import Session
from sqlalchemy import select, update

class UserRepository(UserRepositoryInterface):
    def __init__(self, engine: Engine):
        self.engine = engine
        self.session = Session(engine)

    def save(self, user: User):
        try:
            with self.session as s:
                user_orm = s.query(UserORM).filter_by(id=user.id).first()

                if user_orm:
                    user_orm.name = user.name
                    user_orm.email = user.email
                    user_orm.password = user.password
                    user_orm.blocked = user.blocked
                else:
                    new_user = UserORM(
                        name=user.name,
                        email=user.email,
                        password=user.password,
                        blocked=user.blocked
                    )
                    s.add(new_user)
                
                s.commit()
        except Exception as e:
            s.rollback()

            raise e
    

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

        self.session.close()

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

        self.session.close()

        return user_list