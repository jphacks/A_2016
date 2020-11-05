from datetime import datetime

from sqlalchemy import Column, Integer, String, DateTime, text

from app.db import Base


class Device(Base):
    __tablename__ = "devices"

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        self.item = ''
        self.max = 0
        self.min = 0
        self.weight = 0
        self.color = '#FFFFFF'

    id = Column(String(length=32), primary_key=True)
    item = Column(String(length=255))
    max = Column(Integer)
    min = Column(Integer)
    weight = Column(Integer)
    color = Column(String(length=7))
    expiration_date = Column(DateTime)
