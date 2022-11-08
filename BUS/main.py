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


@app.get("/buses")
def read_buses():
    buses = session.query(BusTable).all()
    return buses

@app.get("/buses/{bus_id}")
def read_bus(bus_id: int):
    bus = session.query(BusTable).filter(BusTable.id == bus_id).first()
    return bus

@app.post("/bus")
async def create_bus(bus: str, bus_name: str):

    bus = BusTable()
    bus.bus = bus
    bus.bus_name = bus_name

    session.add(bus)
    session.commit()

    return f"{bus} created..."

@app.put("/buses")
async def update_stations(buses: List[Bus]):

    for i in buses:
        bus = session.query(BusTable).filter(BusTable.id == i.id).first()
        bus.bus = i.bus
        bus.bus_name = i.bus_name
        session.commit()

    return f"{buses[0].bus} updated..."


@app.delete("/bus")
async def delete_stations(busid: int):

    bus = session.query(BusTable).filter(BusTable.id == busid).delete()
    session.commit()

    return f"Bus deleted..."
