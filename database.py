from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from config import POST_USER, POST_PASSWORD, POST_HOST, POST_DATABASE
from config import MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE

""" SQLALCHEMY_DATABASE_URL = 'sqlite:///./todo.db' """
SQLALCHEMY_DATABASE_URL = f"postgresql://{POST_USER}:{POST_PASSWORD}@{POST_HOST}/{POST_DATABASE}"
# SQLALCHEMY_DATABASE_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)
Base = declarative_base()
