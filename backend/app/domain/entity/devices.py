from datetime import datetime
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, text

from app.db import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(String(length=32), primary_key=True)
    item = Column(String(length=255))
    max = Column(Integer)
    min = Column(Integer)
    weight = Column(Integer)
    color = Column(String(length=7))
    expiration_date = Column(DateTime)
