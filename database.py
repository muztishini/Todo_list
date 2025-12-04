from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import create_engine
from config import USER, PASSWORD, HOST, DATABASE

SQLALCHEMY_DATABASE_URL = "sqlite:///./todo.db"
# SQLALCHEMY_DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{DATABASE}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autoflush=False, bind=engine, autocommit=False)
Base = declarative_base()
