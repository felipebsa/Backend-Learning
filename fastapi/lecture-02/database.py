from sqlalchemy import create_engine, Column, Integer, String, Float, Boolean
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./database.db"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    value = Column(Float)
    detail = Column(String)
    expired = Column(Boolean, default=False)