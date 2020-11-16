from typing import List

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.db import Database


def new_router(db: Database):
    router = APIRouter()

    class GetContainersResContainer(BaseModel):
        id: str
        image: str
        name: str
        max: int
        min: int

    class GetContainersRes(BaseModel):
        containers: List[GetContainersResContainer]

    @router.get("/containers")
    def get_containers(ssn: Session = Depends(db.get_db)):
        return GetContainersRes(containers=[
            GetContainersResContainer(
                id="C51CD0F5",
                image="https://i.picsum.photos/id/202/200/200.jpg",
                name="牛乳パック",
                max=1040,
                min=40
            ),
            GetContainersResContainer(
                id="C51CD0F6",
                image="https://i.picsum.photos/id/202/200/200.jpg",
                name="500mlペットボトル",
                max=540,
                min=40
            )
        ])

    return router
