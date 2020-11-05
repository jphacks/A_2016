from datetime import datetime
from typing import Optional, List

import sqlalchemy
from pydantic import validator
from sqlalchemy.orm import Session

from app.domain import entity
from app.domain.schemas import DeviceBase, validate_item, validate_min, validate_nat, validate_color, \
    validate_expiration_date


class DeviceCreate(DeviceBase):
    item: str
    max: int
    min: int
    color: str
    expiration_date: Optional[str]

    _validate_name = validator('item', allow_reuse=True)(validate_item)
    _validate_min = validator('min', allow_reuse=True)(validate_min)
    _validate_min_nat = validator('min', allow_reuse=True)(validate_nat)
    _validate_max = validator('max', allow_reuse=True)(validate_nat)
    _validate_color = validator('color', allow_reuse=True)(validate_color)
    _validate_expiration_date = validator(
        'expiration_date', allow_reuse=True)(validate_expiration_date)


def create_device(db: Session, device: DeviceCreate):
    try:
        expiration_date = datetime.fromisoformat(device.expiration_date)
    except:
        expiration_date = None
    db_device = entity.Device(
        id=device.id,
        item=device.item,
        max=device.max,
        min=device.min,
        color=device.color,
        weight=0,
        expiration_date=expiration_date
    )

    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def get_devices_by_id(db: Session, device_id: str) -> entity.Device:
    return db.query(entity.Device).filter(entity.Device.id == device_id).first()


def get_all_devices(db: Session) -> List[entity.Device]:
    return db.query(entity.Device).all()


class DeviceUpdate(DeviceBase):
    item: Optional[str]
    max: Optional[int]
    min: Optional[int]
    weight: Optional[int]
    color: Optional[str]
    expiration_date: Optional[str]

    _validate_name = validator('item', allow_reuse=True)(validate_item)
    _validate_min = validator('min', allow_reuse=True)(validate_min)
    _validate_min_nat = validator('min', allow_reuse=True)(validate_nat)
    _validate_max = validator('max', allow_reuse=True)(validate_nat)
    _validate_weight_nat = validator('weight', allow_reuse=True)(validate_nat)
    _validate_color = validator('color', allow_reuse=True)(validate_color)
    _validate_expiration_date = validator(
        'expiration_date', allow_reuse=True)(validate_expiration_date)


def update_device(db: Session, params: DeviceUpdate):
    query = db.query(entity.Device)
    device_update: Optional[entity.Device] = query.filter(
        entity.Device.id == params.id).first()
    if device_update is None:
        return None
    if params.item is not None:
        device_update.item = params.item
    if params.max is not None:
        device_update.max = params.max
    if params.min is not None:
        device_update.min = params.min
    if params.weight is not None:
        device_update.weight = params.weight
    if params.color is not None:
        device_update.color = params.color
    if params.expiration_date is not None:
        device_update.expiration_date = params.expiration_date
    db.commit()
    db.refresh(device_update)
    return device_update


def delete_device(db: Session, device_id: str):
    query = db.query(entity.Device)
    device: Optional[entity.Device] = query.filter(
        entity.Device.id == device_id).first()
    if device is None:
        return False
    db.delete(device)
    db.commit()
    return True
