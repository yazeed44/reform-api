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




with open("dataframe.geojson") as f:
    dataframe = json.load(f)


@app.get("/")
async def root():
    return dataframe
