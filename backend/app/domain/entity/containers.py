from sqlalchemy import Column, String, Integer

from app.db import Base


class Container(Base):
    __tablename__ = "containers"

    id = Column(String(length=32), primary_key=True)
    name = Column(String(length=255), nullable=False)
    image = Column(String(length=1024), nullable=False)
    max = Column(Integer, nullable=False, default=0)
    min = Column(Integer, nullable=False, default=0)
