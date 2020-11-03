from app.db import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Device(Base):
    __tablename__ = "devices"

    id = Column(String(length=32), primary_key=True)
    item = Column(String(length=255))
    max = Column(Integer)
    min = Column(Integer)
    weight = Column(Integer)
