from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine("sqlite:///database.db")
Base = declarative_base()
session_base = sessionmaker(bind=engine)

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String(50))
    done = Column(Boolean, default=False)

    def __repr__(self):
        return f"<{self.id}> | age={self.title} | id={self.done}"
    
Base.metadata.create_all(engine)