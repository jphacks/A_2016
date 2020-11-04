import traceback
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from .db import Database

from .domain import schemas, repository

# TODO: get from env
DATABASE_URL = "postgresql://pizza:pizzatabetai@postgres/pizza"

db = Database(DATABASE_URL)

# server = "ec2-3-208-224-152.compute-1.amazonaws.com"
# port = "5432"
# dbname = "d4v2bqr9sa4l5v"
# user = "rwuiymiymxajli"
# password = "f37f88c526282ce854d6356b27bc0ae75fd92e23bef0a83f76b81974d7299a26"
# conn = psycopg2.connect(
#     "host=" + server + " port=" + port + " dbname=" + dbname + " user=" + user + " password=" + password)
# cursor = conn.cursor()
# try:
#     cursor.execute('CREATE TABLE devices (id char(16),name char(16),max real,min real,cur real, expdate real)')
# except:
#     print("DB already exists")

app = FastAPI()


class PostItemsReq(BaseModel):
    device_id: str
    item: str
    max: int
    min: int


@app.post("/items", status_code=status.HTTP_201_CREATED)
def post_items(req: PostItemsReq, ssn: Session = Depends(db.get_db)):
    # TODO: 値のバリデーション
    try:
        repository.create_device(
            ssn,
            schemas.DeviceCreate(
                id=req.device_id,
                item=req.item,
                max=req.max,
                min=req.min,
            ),
        )
        return {}
    except Exception as err:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail='Error: %s' % err,
        )


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

# @app.get("/reset", status_code=status.HTTP_201_CREATED)
# def post_items():
#     try:
#         cursor.execute('DELETE FROM devices')
#         conn.commit()
#     except Exception as e:
#         print("DB error", e)
#         conn.rollback()
#         pass
#     return {"text": "reseted"}
