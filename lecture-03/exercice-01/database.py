from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.db")
Base = declarative_base()
session_base = sessionmaker(engine)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(40))
    age = Column(Integer)

    def __repr__(self):
        return f"<{self.name}> | age={self.age} | id={self.id}"

Base.metadata.create_all(engine)