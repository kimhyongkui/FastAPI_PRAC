from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class name(BaseModel):
    name: str

class age(BaseModel):
    age: int

class Item(BaseModel):
    name: str | None = None
    age: float | None = None


items = {
    "Kim": {"name": "김연아", "age": 33},
    "Park": {"name": "박지성", "age": 42},
    "Son": {"name": "손흥민", "age": 31},
}


@app.get("/user/", tags=["User"])
async def read_users():
    result = "내 이름은 김형규고 나이는 32살입니다."
    return result


@app.post("/user/", tags=["User"])
async def users(name: name, age: age):
    result = f"내 이름은 {name.name}고 나이는 {age.age}살입니다."
    return result


@app.patch("/user/", tags=["User"])
async def update_users():
    result = "내 이름은 누구고 나이는 몇살입니다."
    return result


@app.delete("/user/", tags=["User"])
async def items():
    result = "내 이름은 누구고 나이는 몇살입니다."
    return result

@app.get("/items/", tags=["공부"], response_model=Item)
async def read_item(item_id):
    return items[item_id]
