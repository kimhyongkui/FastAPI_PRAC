# from fastapi import FastAPI
# from pydantic import BaseModel
# from typing import List
# from starlette.middleware.cors import CORSMiddleware
#
# from database import session
# from model import UserTable, User
#
# import requests
#
# app = FastAPI()
#
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allowwheaders=["*"],
# )
#
# db = []
#
# class City(BaseModel):
#     name: str
#     timezone: str
#
# class CityModify(BaseModel):
#     id: int
#     name: str
#     timezone: str
#
#
#
# @app.get('/cities')
# def get_cities():
#     results = []
#     for city in db:
#         str = f"http://worldtimeapi.org/api/timezone/{city['timezone']}"
#         print(str)
#         r = requests.get(str)
#         cur_time = r.json()['datetime']
#         results.append({'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time})
#
#     return results
#
#
# @app.get('/cities/{city_id}')
# def get_city(city_id: int):
#     city = db[city_id]
#     r = requests.get(f"http://worldtimeapi.org/api/timezone/{city['timezone']}")
#     cur_time = r.json()['datetime']
#     return {'name':city['name'], 'timezone':city['timezone'], 'current_time': cur_time}
#
#
# @app.post('/cities')
# def create_city(city: City):
#     db.append(city.dict())
#     return db
#
# @app.put('/cities')
# def modify_city(city: CityModify):
#
#     db[city.id] = { 'name': city.name, 'timezone': city.timezone }
#
#     return db[city.id]
#
# @app.delete('/cities/{city_id}')
# def delete_city(city_id: int):
#     db.pop(city_id)
#     return {}
#
#
#
#
