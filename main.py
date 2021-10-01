import json

from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    with open("districts.json") as f:
        districts = json.load(f)
        return districts
