import requests, xmltodict, json


key = "sh%2F1QzN2LTDtEC%2BJVBs0xY8tKrpfWk%2F5uHe88YcwMk59ICjn2dhJ6tSBL5DnWTkBDlyn5YRqJR1IQPXex6TqFQ%3D%3D"
url = "http://ws.bus.go.kr/api/rest/busRouteInfo/getBusRouteList?ServiceKey={}".format(key)
# .format을 이용해서 포매팅

content = requests.get(url).content # GET요청
dict = xmltodict.parse(content) # XML을 dictionary로 파싱


jsonString = json.dumps(dict['ServiceResult']['msgBody']['itemList'], ensure_ascii=False) # dict을 json으로 변환
jsonObj = json.loads(jsonString) # JSON 디코딩, json을 dict으로 변환


# getBusRouteID( 매개변수는 버스 번호)
# 	bus_dict = {}
# 	for문 버스 숫자 in jsonObj:
# 	bus_name = bus['busRouteNm']
# 	bus_Id = bus['busRouteId']
# 	버스 네임과 버스 아이디를 묶고 딕셔너리화 시켜서
# 	bus_dict에 집어넣는다
# 	만약 버스번호가 버스 네임과 같다면 버스아이디를 출력시킨다
# 	출력 f'{bus_name}의 버스ID는 {bus_Id}입니다.'

def getBusRouteId(bus_number):
    bus_number = str(bus_number)
    bus_dict = {}
    for bus in jsonObj:
        bus_name = bus['busRouteNm']
        bus_Id = bus['busRouteId']
        bus_dict[bus_name] = bus_Id
        if bus_number == bus_name:
            print(f'{bus_name}의 버스ID는 {bus_Id}입니다.')

    return bus_dict

getBusRouteId(6001)



