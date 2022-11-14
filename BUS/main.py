from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from typing import List
from db import session
from models import BusTable, Bus


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
    bus = session.query(BusTable).filter(BusTable.bus_id == bus_id).first()
    return bus

@app.post("/bus")
async def create_bus(bus_name: str, bus_id: int):

    bus = BusTable()
    bus.bus_name = bus_name
    bus.bus_id = bus_id

    session.add(bus)
    session.commit()

    return f"{bus_name} created..."

@app.put("/buses")
async def update_stations(buses: List[Bus]):

    for i in buses:
        bus = session.query(BusTable).filter(BusTable.bus_id == i.bus_id).first()
        bus.bus_id = i.bus_id
        bus.bus_name = i.bus_name
        session.commit()

    return f"{buses[0].bus} updated..."


@app.delete("/bus")
async def delete_stations(bus_id: int):

    bus = session.query(BusTable).filter(BusTable.id == bus_id).delete()
    session.commit()

    return f"Bus deleted..."
