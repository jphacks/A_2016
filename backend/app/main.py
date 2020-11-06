import os
import traceback
from typing import List, Optional

from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from .db import Database
from .domain import repository
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
    color: str
    expiration_date: str  # ISO8601


@app.post("/devices", status_code=status.HTTP_201_CREATED)
def post_devices(req: PostDevicesReq, ssn: Session = Depends(db.get_db)):
    # すでに存在するデバイスか確認
    device = repository.get_devices_by_id(ssn, req.device_id)
    color = req.color or "#FFFFFF"
    expiration_date = req.expiration_date or None

    try:
        if device is None:
            repository.create_device(
                ssn,
                DeviceCreate(
                    id=req.device_id,
                    item=req.item,
                    max=req.max,
                    min=req.min,
                    color=color,
                    expiration_date=expiration_date,
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
                    color=color,
                    expiration_date=expiration_date,
                )
            )
        return {}
    except ValueError as err:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='%s' % err
        )
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
    color: Optional[str]
    expiration_date: Optional[str]


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
        exp = d.expiration_date.isoformat() if d.expiration_date is not None else None
        try:
            percentage = 100 * (weight - d.min) / (d.max - d.min)
        except ZeroDivisionError:
            percentage = 0
        res_devices.append(GetDevicesResDevice(
            device_id=d.id,
            item=d.item,
            weight=weight,
            percentage=percentage,
            color=d.color,
            expiration_date=exp
        ))
    return GetDevicesRes(devices=res_devices)


@app.delete("/devices/{device_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_devices(device_id: str, ssn: Session = Depends(db.get_db)):
    if not repository.delete_device(ssn, device_id):
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
