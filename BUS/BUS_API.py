import requests, xmltodict, json
import os
from dotenv import load_dotenv



load_dotenv()
key = os.getenv('key')

url = f"http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={key}"



content = requests.get(url).content # GET요청
dict=xmltodict.parse(content) # XML을 dictionary로 파싱


jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
jsonObj = json.loads(jsonString) # JSON 디코딩, json을 dict으로 변환


for i in range(len(jsonObj)):
    print(jsonObj[i]['stationNm']) # stationNm : 정류소명

