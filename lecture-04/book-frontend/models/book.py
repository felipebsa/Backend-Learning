from database import Base
from sqlalchemy import Column, String, Boolean, Integer

class Book(Base):
    __tablename__ = "Books"

    id = Column(Integer, primary_key=True)
    title = Column(String(120))
    author = Column(String(60))
    read = Column(Boolean, default=False)

    def __repr__(self):
        return f"<{self.id}> | age={self.title} | read={self.read}"