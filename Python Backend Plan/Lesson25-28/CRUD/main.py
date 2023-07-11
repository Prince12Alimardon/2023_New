from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# fake database
database = []


class Task(BaseModel):
    id: int
    title: str
    description: str


@app.post("/tasks/")
def create_task(task: Task):
    """
    Create a new task
    """
    database.append(task)
    return task


@app.get("/tasks/{task_id}")
def read_task(task_id: int):
    """
    Get a task by ID
    """
    for task in database:
        if task.id == task_id:
            return task
    return {"error": "Task not found"}


@app.get("/tasks/")
def read_tasks():
    """
    Get all tasks
    """
    return database


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    """
    Update a task by ID
    """
    for i, t in enumerate(database):
        if t.id == task_id:
            database[i] = task
            return {"message": "Task updated successfully"}
    return {"error": "Task not found"}


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    """
    Delete a task by ID
    """
    for i, task in enumerate(database):
        if task.id == task_id:
            database.pop(i)
            return {"message": "Task deleted successfully"}
    return {"error": "Task not found"}
