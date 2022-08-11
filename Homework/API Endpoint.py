from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

class Body(BaseModel):
    name: str

@app.get("/name/", tags=["name"])
async def items():
    result = "내 이름은 누구입니다."
    return result


@app.post("/name/", tags=["name"])
async def items(name: Body):
    result = f"내 이름은 {name.name}입니다."
    return result

@app.put("/name/", tags=["name"])

@app.delete("/name/", tags=["name"])