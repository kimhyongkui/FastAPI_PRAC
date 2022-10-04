from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

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