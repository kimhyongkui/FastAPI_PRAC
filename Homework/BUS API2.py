from pydantic import BaseModel
from fastapi import FastAPI
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests, xmltodict, json

app = FastAPI()

url = "http://ws.bus.go.kr/api/rest/buspos/getBusPosByRtid?serviceKey=sh%2F1QzN2LTDtEC%2BJVBs0xY8tKrpfWk%2F5uHe88YcwMk59ICjn2dhJ6tSBL5DnWTkBDlyn5YRqJR1IQPXex6TqFQ%3D%3D&busRouteId=100100118"