from sqlalchemy import create_engine, Column, String, Integer, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine("sqlite:///database.db")
Base = declarative_base()
session_base = sessionmaker(bind=engine)

class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    title = Column(String(120))
    author = Column(String(60))
    read = Column(Boolean, default=False)

    def __repr__(self):
        return f"<{self.id}> | age={self.title} | read={self.read}"

Base.metadata.create_all(engine)