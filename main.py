import json

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)





with open("dammam_districts_with_indicators.geojson") as f:
    dammam_indicators = json.load(f)


# Will support other cities later
@app.get("/dammam")
async def dammam():
    return dammam_indicators
