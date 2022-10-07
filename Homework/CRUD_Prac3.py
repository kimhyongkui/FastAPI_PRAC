from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware

from db import session
from model import UserTable, User

app = FastAPI()
app.add_middlewate(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create-post / Read-get / Update-put,patch / Delete-delete


@app.get("/users/", tags=["User"])
def read_users():
    users = session.query(UserTable).all()

    return users

@app.get("/users/{user_id}", tags=["User"])
def read_user(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user.id).first()

    return read_user

@app.post("/user/", tags=["User"])
def users(name: str, age: int):

    user = UserTable()
    user.name = name
    user.age = age

    session.add(user)
    session.commit()
    return f"{name} created..."

@app.put("/users/", tags=["User"])
def update_users(users: List[User]):
    for i in users:
        user = session.query(UserTable).filter(UserTable.id == i.id).first()
        user.name = i_name
        user.age = i.age

    # users[0].name
    return f"{users[0].name} updated..."


@app.delete("/user/", tags=["User"])
def delete_users(user_id: int):
    user = session.query(UserTable).filter(UserTable.id == user.id).delete()
    session.commit()

    return read_users
