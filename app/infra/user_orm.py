from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, VARCHAR, create_engine, Integer
from app.infra.base_orm import BaseORM


class UserORM(BaseORM):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[VARCHAR] = mapped_column(VARCHAR(30))
    email: Mapped[VARCHAR] = mapped_column(VARCHAR(45), unique=True)
    password: Mapped[String] = mapped_column(VARCHAR(16))
    blocked: Mapped[Integer] = mapped_column(Integer)
