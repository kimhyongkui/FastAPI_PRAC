from fastapi import FastAPI
from typing import List
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import requests, xmltodict, json

app = FastAPI()


key = "sh%2F1QzN2LTDtEC%2BJVBs0xY8tKrpfWk%2F5uHe88YcwMk59ICjn2dhJ6tSBL5DnWTkBDlyn5YRqJR1IQPXex6TqFQ%3D%3D"
url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?ServiceKey={}&busRouteId=100100118".format(key)




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

content = requests.get(url).content # GET요청
dict=xmltodict.parse(content) # XML을 dictionary로 파싱
#파싱은 어떤 페이지(문서, html 등)에서 내가 원하는 데이터를 특정 패턴이나 순서로 추출해 가공하는 것

jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
jsonObj = json.loads(jsonString) # json을 dict으로 변환

for i in range(len(jsonObj)):
    print(jsonObj[i]['stationNm']) # stationNm : 정류소명


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
