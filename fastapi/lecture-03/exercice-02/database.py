from sqlalchemy import create_engine, column, String, Integer
from sqlalchemy.orm import create_session, declarative_base

engine = create_engine("sqlite:///database.py")
Base = declarative_base()
session_base = create_session(engine)

