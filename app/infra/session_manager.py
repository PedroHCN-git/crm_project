from app.infra.base_orm import BaseORM
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()
ENV = os.getenv('ENV')
DB_URL = os.getenv(f'DB_{ENV}_URL')

engine = create_engine(DB_URL)
BaseORM.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)