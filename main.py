from fastapi import FastAPI, Query
import uvicorn

import db

app = FastAPI()
users = []

@app.get("/get_users/")
def get_users():
    return {"users": users}

@app.post("/add_user/")
def add_user(name: str = Query()):
    if name not in db.data:
        users.append(name)
        return dict(msg="Дані додано.")
    
@app.delete("/del_user/")
def del_user(name: str = Query()):
    if name not in users:
        return dict(msg="Немає такого ім'я")
    users.remove(name)
    return dict(msg="Ім'я видалено.")

if __name__ == "__main__":
    uvicorn.run("main:app")