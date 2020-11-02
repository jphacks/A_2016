from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status
import pandas as pd
import psycopg2

server="ec2-3-208-224-152.compute-1.amazonaws.com"
port="5432"
dbname="d4v2bqr9sa4l5v"
user="rwuiymiymxajli"
password="f37f88c526282ce854d6356b27bc0ae75fd92e23bef0a83f76b81974d7299a26"
conn=psycopg2.connect("host="+server+" port="+port+" dbname="+dbname+" user="+user+" password="+password)
try:
    cursor.execute('CREATE TABLE devices (id char(16),name char(16),max real,min real,cur real, expdate real)')
except:
    print("DB already exists")
cursor = conn.cursor()

app = FastAPI()
class PostStatesReq(BaseModel):
    device_id: str
    weight: int


@app.post("/states", status_code=status.HTTP_204_NO_CONTENT)
def post_states(req: PostStatesReq):
    print(req)
    return {}


class GetStatesResState(BaseModel):
    device_id: str
    item: str
    weight: int
    percentage: int


class GetStatesRes(BaseModel):
    states: List[GetStatesResState]


@app.get("/states", response_model=GetStatesRes)
def get_states():
    # TODO: replace with real data
    return {"states": [
        {
            "device_id": "5CDCD567",
            "item": "牛乳",
            "weight": 500,
            "percentage": 52
        },
        {
            "device_id": "5CDCD568",
            "item": "コーヒー牛乳",
            "weight": 500,
            "percentage": 52
        }
    ]}

#Register item
class PostItemsReq(BaseModel):
    device_id: str
    item: str
    max: int
    min: int
    expdate: int#unix time


@app.post("/items", status_code=status.HTTP_201_CREATED)
def post_items(req: PostItemsReq):
    print(req)

    return {}
