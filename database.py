from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = 'postgresql://postgres:bgfds123@localhost:5432/db_escola' # URL do DataBase

engine = create_engine(DATABASE_URL) # Motor do DataBase

Base = declarative_base() # Base para as tabelas

SessionLocal = sessionmaker(bind=engine) # Sessão do DataBase