from typing import Optional, List

from sqlalchemy.orm import Session

from app.domain import entity
from app.domain.schemas import DeviceBase


class DeviceCreate(DeviceBase):
    item: str
    max: int
    min: int


def create_device(db: Session, device: DeviceCreate):
    db_device = entity.Device(
        id=device.id,
        item=device.item,
        max=device.max,
        min=device.min,
    )

    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device


def get_all_devices(db: Session) -> List[entity.Device]:
    return db.query(entity.Device).all()


class DeviceUpdate(DeviceBase):
    item: Optional[str]
    max: Optional[int]
    min: Optional[int]
    weight: Optional[int]


def update_device(db: Session, params: DeviceUpdate):
    query = db.query(entity.Device)
    device_update: Optional[entity.Device] = query.filter(entity.Device.id == params.id).first()
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
    db.commit()
    db.refresh(device_update)
    return device_update
