# Importando dependencias
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv() # Carrega o dotenv

DATABASE_URL = os.getenv('DATABASE_URL') # Carrega a URL que esta guardada no .env

engine = create_engine(DATABASE_URL) # Motor do DataBase

Base = declarative_base() # Base para as tabelas

SessionLocal = sessionmaker(bind=engine) # Sessão do DataBase