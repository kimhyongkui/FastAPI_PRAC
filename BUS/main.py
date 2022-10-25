from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware

from database import session
from models import UserTable, User

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/users")
def read_users():

    return

@app.get("/users/{user_id}")
def read_user():

    return

@app.post("/user")
async def create_user():

    return

@app.put("/users")
async def update_users():


    return


@app.delete("/user")
async def delete_users():

    return
