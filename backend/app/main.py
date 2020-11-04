import os
import traceback
from typing import List

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from .db import Database

from .domain import schemas, repository
from .domain.repository import DeviceCreate, DeviceUpdate

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
            DeviceCreate(
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
def post_states(req: PostStatesReq, ssn: Session = Depends(db.get_db)):
    # TODO: validation
    try:
        device = repository.update_device(
            ssn,
            DeviceUpdate(
                id=req.device_id,
                weight=req.weight,
            ),
        )
    except Exception as err:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Error: %s' % err,
        )

    if device is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='device_id: %s is not found' % req.device_id,
        )

    return Response(status_code=status.HTTP_204_NO_CONTENT)


class GetStatesResState(BaseModel):
    device_id: str
    item: str
    weight: int
    percentage: float


class GetStatesRes(BaseModel):
    states: List[GetStatesResState]


@app.get("/states", response_model=GetStatesRes)
def get_states(ssn: Session = Depends(db.get_db)):
    try:
        devices = repository.get_all_devices(ssn)
    except Exception as err:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Error: %s' % err,
        )
    states: List[GetStatesResState] = []
    for d in devices:
        weight = d.weight or 0
        percentage = 100 * (weight - d.min) / (d.max - d.min)
        states.append(GetStatesResState(
            device_id=d.id,
            item=d.item,
            weight=weight,
            percentage=percentage
        ))
    return GetStatesRes(states=states)
