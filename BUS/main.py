
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
import requests, xmltodict, json
from typing import List
from db import session
from models import UserTable, User

app = FastAPI()

key = "sh%2F1QzN2LTDtEC%2BJVBs0xY8tKrpfWk%2F5uHe88YcwMk59ICjn2dhJ6tSBL5DnWTkBDlyn5YRqJR1IQPXex6TqFQ%3D%3D"
url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?ServiceKey={}&busRouteId=100100118".format(key)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

content = requests.get(url).content
dict=xmltodict.parse(content)


jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False)
jsonObj = json.loads(jsonString)

for i in range(len(jsonObj)):
    print(jsonObj[i]['stationNm'])


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
