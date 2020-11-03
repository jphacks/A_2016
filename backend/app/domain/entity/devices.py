from .entity import Base
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String


class Device(Base):
    __tablename__ = "devices"

    id = Column(String, primary_key=True)
    item = Column(String)
    max = Column(Integer)
    min = Column(Integer)
    weight = Column(Integer)
