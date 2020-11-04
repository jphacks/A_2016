import os
import traceback
from typing import List

import psycopg2
from fastapi import FastAPI, Depends, HTTPException
from psycopg2 import errors
from pydantic import BaseModel
from sqlalchemy import exc
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


class PostDevicesReq(BaseModel):
    device_id: str
    item: str
    max: int
    min: int


@app.post("/devices", status_code=status.HTTP_201_CREATED)
def post_devices(req: PostDevicesReq, ssn: Session = Depends(db.get_db)):
    # TODO: 値のバリデーション
    # すでに存在するデバイスか確認
    device = repository.get_devices_by_id(ssn, req.device_id)
    try:
        if device is None:
            repository.create_device(
                ssn,
                DeviceCreate(
                    id=req.device_id,
                    item=req.item,
                    max=req.max,
                    min=req.min,
                ),
            )
        else:
            repository.update_device(
                ssn,
                DeviceUpdate(
                    id=req.device_id,
                    item=req.item,
                    max=req.max,
                    min=req.min,
                )
            )
        return {}
    except Exception as err:
        traceback.print_exc()
        raise HTTPException(
            status_code=500,
            detail='Error: %s' % err,
        )


class PutDevicesWeightReq(BaseModel):
    device_id: str
    weight: int


@app.put("/devices/weight", status_code=status.HTTP_204_NO_CONTENT)
def post_states(req: PutDevicesWeightReq, ssn: Session = Depends(db.get_db)):
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


class GetDevicesResDevice(BaseModel):
    device_id: str
    item: str
    weight: int
    percentage: float


class GetDevicesRes(BaseModel):
    devices: List[GetDevicesResDevice]


@app.get("/devices", response_model=GetDevicesRes)
def get_states(ssn: Session = Depends(db.get_db)):
    try:
        devices = repository.get_all_devices(ssn)
    except Exception as err:
        traceback.print_exc()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail='Error: %s' % err,
        )
    res_devices: List[GetDevicesResDevice] = []
    for d in devices:
        weight = d.weight or 0
        try:
            percentage = 100 * (weight - d.min) / (d.max - d.min)
        except ZeroDivisionError:
            percentage = 0
        res_devices.append(GetDevicesResDevice(
            device_id=d.id,
            item=d.item,
            weight=weight,
            percentage=percentage
        ))
    return GetDevicesRes(devices=res_devices)
