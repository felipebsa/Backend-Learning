from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String
from database import Base

class vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id: Mapped[int] = mapped_column(primary_key=True)
    vehicle_make: Mapped[str] = mapped_column(String(100))
    vehicle_model: Mapped[str] = mapped_column(String(100))
    vehicle_year: Mapped[int] = mapped_column()
    vehicle_chassi: Mapped[str] = mapped_column(unique=True)
    vehicle_default: Mapped[bool] = mapped_column(default=True)