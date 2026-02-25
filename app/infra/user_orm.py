from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, VARCHAR

class Base(DeclarativeBase):
    pass

class UserORM(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[VARCHAR] = mapped_column(VARCHAR(30))
    email: Mapped[VARCHAR] = mapped_column(VARCHAR(45), unique=True)
    password: Mapped[String] = mapped_column(VARCHAR(16))
