from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
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
@app.get("/users/{item_id}", tags=["공부"], response_model=Item)
async def read_item(item_id: str):
    return items[item_id]

@app.put("/users/{item_id}", tags=["공부"], response_model=Item)
async def update_users(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded



@app.get("/items/{item_id}", response_model=Item)
async def read_item(item_id: str):
    return items[item_id]


@app.put("/items/{item_id}", response_model=Item)
async def update_item(item_id: str, item: Item):
    update_item_encoded = jsonable_encoder(item)
    items[item_id] = update_item_encoded
    return update_item_encoded



# def Output(a, b):
#     add = a + b
#     print(a,'+',b,'=',add,'입니다.', sep='')
#     return add
#
# print(Output(3,8))