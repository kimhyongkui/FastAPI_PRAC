from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from typing import List
from db import session
from models import StationTable, Station

app = FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/stations")
def read_stations():
    stations = session.query(StationTable).all()
    return stations

@app.get("/stations/{station_id}")
def read_station(station_id: int):
    station = session.query(StationTable).filter(StationTable.id == station_id).first()
    return station

@app.post("/station")
async def create_station(bus: str, station_name: str):

    station = StationTable()
    station.bus = bus
    station.station_name = station_name

    session.add(station)
    session.commit()

    return f"{bus} created..."

@app.put("/stations")
async def update_stations(stations: List[Station]):

    for i in stations:
        station = session.query(StationTable).filter(StationTable.id == i.id).first()
        station.bus = i.bus
        station.station_name = i.station_name
        session.commit()

    return f"{stations[0].bus} updated..."


@app.delete("/station")
async def delete_stations(stationid: int):

    user = session.query(StationTable).filter(StationTable.id == stationid).delete()
    session.commit()

    return f"Station deleted..."
