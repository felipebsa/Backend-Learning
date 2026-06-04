from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from database import engine, Base, session_base, Task

app = FastAPI()
Base.metadata.create_all(engine)

class TaskSchema(BaseModel):
    title: str
    done: bool

@app.get("/")
def Home():
    return {"message": "Fucionou"}
@app.post("/tasks")
def create_task(task: TaskSchema):
    db = session_base()
    db_task = Task(
        title = task.title,
        done = task.done
    )
    db.add(db_task)
    db.commit()
    db.close()
    return {"message": "Task create successful"}

@app.get("/tasks/{id}")
def get_task(id: int):
    db = session_base()
    task = db.query(Task).filter_by(id=id).first()
    if not task:
        raise HTTPException(status_code=404, detail="not found a task")
    return task

@app.get("/tasks")
def get_tasks(done: bool = None):
    db = session_base()
    if done is None:
        return db.query(Task).all()
    return db.query(Task).filter_by(done=done).all()
    