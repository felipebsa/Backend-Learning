from fastapi import FastAPI
from pydantic import BaseModel
from database import Base, engine, session_base, User

app = FastAPI()

Base.metadata.create_all(engine)

class UserSchema(BaseModel):
    name: str
    age: int

@app.post("/register/")
def create_user(user: UserSchema):
    db = session_base()
    db_user = User(
        name=user.name,
        age=user.age
    )
    db.add(db_user)
    db.commit()
    db.close()
    return {"message": "user created"}

@app.get("/users/")
def get_users():
    db = session_base()
    users = db.query(User).all()
    db.close()
    return users
