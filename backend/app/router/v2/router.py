from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import Database


def new_router(db: Database):
    router = APIRouter()

    @router.get("/containers")
    def get_containers(ssn: Session = Depends(db.get_db)):
        return {"msg": 'hello'}

