import traceback
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status

from app.db import Database
from app.domain import repository
from app.domain.schemas.containers import Container


def new_router(db: Database):
    router = APIRouter()

    class GetContainersResContainer(Container):
        pass

    class GetContainersRes(BaseModel):
        containers: List[GetContainersResContainer]

    @router.get("/containers")
    def get_containers(ssn: Session = Depends(db.get_db)):
        try:
            containers = repository.get_all_containers(ssn)
        except Exception as err:
            traceback.print_exc()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error: %s' % err,
            )

        res_containers: List[GetContainersResContainer] = []
        for c in containers:
            try:
                res_containers.append(GetContainersResContainer(
                    id=c.id,
                    image=c.image,
                    name=c.name,
                    max=c.max,
                    min=c.min
                ))
            except ValueError as err:
                raise HTTPException(
                    status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                    detail='Error: %s' % err,
                )

        return GetContainersRes(containers=res_containers)

    return router
