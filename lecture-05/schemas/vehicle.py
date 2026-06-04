from pydantic import BaseModel

class VehicleSchema(BaseModel):
    vehicle_make: str
    vehicle_model: str
    vehicle_year: int
    vehicle_chassi: str
    vehicle_default: bool