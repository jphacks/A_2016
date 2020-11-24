import re
from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from app.domain.repository.user_repository import get_user


class DeviceBase(BaseModel):
    id: str


class Device(DeviceBase):
    item: str
    max: int
    min: int
    weight: int
    color: str
    expiration_date: str
    user_id: Optional[str]

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


def validate_expiration_date(v: Optional[str]) -> Optional[str]:
    if v is None:
        return None
    return datetime.fromisoformat(v.replace('Z', '+00:00')).isoformat()


def validate_user_id(v: Optional[str]) -> Optional[str]:
    if v is None:
        return None
    try:
        get_user(v)
    except:
        return None
    return v
