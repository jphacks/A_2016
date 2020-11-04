from sqlalchemy import Column, Integer, String

from app.db import Base


class Device(Base):
    __tablename__ = "devices"

    id = Column(String(length=32), primary_key=True)
    item = Column(String(length=255))
    max = Column(Integer)
    min = Column(Integer)
    weight = Column(Integer)
