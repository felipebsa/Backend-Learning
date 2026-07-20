from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from database import Base
from datetime import datetime

class Client(Base):
    __tablename__ = "clients"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    cpf: Mapped[str] = mapped_column(String(11), unique=True)
    date: Mapped[datetime] = mapped_column()
    active: Mapped[bool] = mapped_column(default=True)