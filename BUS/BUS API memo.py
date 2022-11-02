from fastapi import FastAPI
import requests, xmltodict, json

app = FastAPI()


key = "sh%2F1QzN2LTDtEC%2BJVBs0xY8tKrpfWk%2F5uHe88YcwMk59ICjn2dhJ6tSBL5DnWTkBDlyn5YRqJR1IQPXex6TqFQ%3D%3D"
# url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getStaionByRoute?ServiceKey={}&busRouteId=100100118".format(key)
url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={}".format(key)
# .format을 이용해서 포매팅

content = requests.get(url).content # GET요청
dict=xmltodict.parse(content) # XML을 dictionary로 파싱


jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
jsonObj = json.loads(jsonString) # JSON 디코딩, json을 dict으로 변환


# for i in range(len(jsonObj)):
#     print(jsonObj[i]['busRouteId'], jsonObj[i]['busRouteNm'])

# def getBusRouteId(strSrch):
#     for i in range(len(jsonObj)):
#         if strSrch == jsonObj[i]['busRouteNm']:
#             strSrch == jsonObj[i]['busRouteId']
#     return jsonObj[i]['busRouteId']

# def getBusRouteId(busRouteNm):
#     for i in range(len(jsonObj)):
#         if jsonObj[i]['busRouteId'] == jsonObj[i]['busRouteNm']:
#             busRouteNm == jsonObj[i]['busRouteId']
#     return jsonObj[i]['busRouteId']

def getBusRouteId():
    for bus in jsonObj:
        bus_name = bus['busRouteNm']
        bus_Id = bus['busRouteId']
        result = f'{bus_name}의 버스ID는 {bus_Id}입니다.'
        print(result)
    return print(result)

print(getBusRouteId())
