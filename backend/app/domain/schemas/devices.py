import re
from datetime import datetime

from pydantic import BaseModel


class DeviceBase(BaseModel):
    id: str


class Device(DeviceBase):
    item: str
    max: int
    min: int
    weight: int
    color: str
    expiration_date: str

    class Config:
        orm_mode = True


def validate_item(item: str) -> str:
    if len(item) == 0:
        raise ValueError('item is required')
    if len(item) > 255:
        raise ValueError('must be shorter than 256')
    return item


def validate_min(min_v: int, values) -> int:
    if min_v > values.get('max'):
        raise ValueError('max must be larger than min')
    return min_v


def validate_nat(v: int) -> int:
    if v < 0:
        raise ValueError('must be larger than 0')
    return v


def validate_color(v: str) -> str:
    if re.fullmatch(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', v) is None:
        raise ValueError('malformed color code: %s' % v)
    return v


def validate_expiration_date(v: str) -> str:
    return datetime.fromisoformat(v.replace('Z', '+00:00')).isoformat()
