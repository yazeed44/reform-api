import json

from fastapi import FastAPI

app = FastAPI()

with open("dataframe.geojson") as f:
    dataframe = json.load(f)


@app.get("/")
async def root():
    return dataframe
