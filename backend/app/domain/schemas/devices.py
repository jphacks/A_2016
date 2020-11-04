from pydantic import BaseModel


class DeviceBase(BaseModel):
    id: str


class Device(DeviceBase):
    item: str
    max: int
    min: int
    weight: int

    class Config:
        orm_mode = True
