import os
import traceback
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from starlette.middleware.cors import CORSMiddleware

from .db import Database

from .domain import schemas, repository

DATABASE_URL = os.environ.get("DATABASE_URL", "")

db = Database(DATABASE_URL)

app = FastAPI()

cors_allow_origins = os.environ.get("CORS_ALLOW_ORIGINS", "").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=cors_allow_origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class PostItemsReq(BaseModel):
    device_id: str
    item: str
    max: int
    min: int


@app.post("/items", status_code=status.HTTP_201_CREATED)
def post_items(req: PostItemsReq, ssn: Session = Depends(db.get_db)):
    # TODO: 値のバリデーション
    # TODO: もし同じIDのdeviceが存在したら、値を更新
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
