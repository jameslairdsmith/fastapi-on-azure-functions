import azure.functions as func

import fastapi

app = fastapi.FastAPI()

@app.get("/sample")
async def index():
    return {
        "info": "Try /hello/James for parameterized route.",
    }

@app.get("/hello/{name}")
async def get_name(name: str):
    return {
        "name": name,
    }

@app.get("/add/{int1}/{int2}")
async def add(int1: int, int2: int):
    return {
        "result": int1 + int2,
    }


@app.get("/mult/{int1}/{int2}")
async def mult(int1: int, int2: int):
    return {
        "result": int1 * int2,
    }

