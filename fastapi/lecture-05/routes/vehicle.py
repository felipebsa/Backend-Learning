from fastapi import APIRouter, HTTPException
from database import Session_Local
from models.vehicle import vehicle
from schemas.vehicle import VehicleSchema

router = APIRouter()

@router.get("/")
def home():
    return {"message": "successful home"}
    
@router.get("/vehicles/{id}")
def get_vehicle(id: int):
    db = Session_Local()
    db_vehicle = db.query(vehicle).filter_by(id=id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="id not found")
    db.close()
    return {"message": db_vehicle}

@router.get("/vehicles")
def get_vehicles():
    db = Session_Local()
    db_vehicle = db.query(vehicle).all()
    db.close()
    return {"message": db_vehicle}

@router.post("/register_vehicle")
def create_vehicle(Vehicle: VehicleSchema):
    db = Session_Local()
    db_vehicle = vehicle(
        vehicle_make = Vehicle.vehicle_make,
        vehicle_model = Vehicle.vehicle_model,
        vehicle_year = Vehicle.vehicle_year,
        vehicle_chassi = Vehicle.vehicle_chassi,
        vehicle_default = Vehicle.vehicle_default
    )
    db.add(db_vehicle)
    db.commit()
    db.close()
    return {"message": "successful create_vehicle"}

@router.delete("/vehicle_delete/{id}")
def delete_vehicle(id: int):
    db = Session_Local()
    db_vehicle = db.query(vehicle).filter_by(id=id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="not found id")
    db.delete(db_vehicle)
    db.commit()
    db.close()
    return {"message": "successful delete_vehicle"}

@router.put("/vehicle_update/{id}")
def update_vehicle(id: int, Vehicle: VehicleSchema):
    db = Session_Local()
    db_vehicle = db.query(vehicle).filter_by(id=id).first()
    if db_vehicle is None:
        raise HTTPException(status_code=404, detail="not found id")
    db_vehicle.vehicle_make = Vehicle.vehicle_make
    db_vehicle.vehicle_model = Vehicle.vehicle_model
    db_vehicle.vehicle_year = Vehicle.vehicle_year
    db_vehicle.vehicle_chassi = Vehicle.vehicle_chassi
    db_vehicle.vehicle_default = Vehicle.vehicle_default
    db.commit()
    db.close()
    return {"message": "successful update_vehicle"}