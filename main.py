import json

from fastapi import FastAPI

app = FastAPI()

with open("dammam_districts_with_indicators.geojson") as f:
    dammam_indicators = json.load(f)


# Will support other cities later
@app.get("/dammam")
async def dammam():
    return dammam_indicators
