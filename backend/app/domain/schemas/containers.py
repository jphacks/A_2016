import re

from pydantic import BaseModel, validator


def validate_image(image: str) -> str:
    if re.fullmatch(r"https?://[\w!?/+\-_~;.,*&@#$%()'[\]]+", image) is None:
        raise ValueError('malformed image url: %s' % image)
    return image


def validate_name(name: str) -> str:
    if len(name) == 0:
        raise ValueError('name is required')
    return name


def validate_min(min_v: int, values) -> int:
    if min_v > values.get('max'):
        raise ValueError('max must be larger than min')
    return min_v


def validate_nat(v: int) -> int:
    if v < 0:
        raise ValueError('must be larger than 0')
    return v


class ContainerBase(BaseModel):
    id: str
    image: str
    name: str
    max: int
    min: int

    _validate_image = validator('image', allow_reuse=True)(validate_image)
    _validate_name = validator('name', allow_reuse=True)(validate_name)
    _validate_max = validator('max', allow_reuse=True)(validate_nat)
    _validate_min = validator('min', allow_reuse=True)(validate_min)


class Container(ContainerBase):
    class Config:
        orm_mode = True
