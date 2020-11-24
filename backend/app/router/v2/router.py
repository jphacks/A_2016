import traceback
from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from sqlalchemy.orm import Session
from starlette import status
import requests
from app.db import Database
from app.domain import repository
from app.domain.repository import DeviceCreate, DeviceUpdate
from app.domain.repository.user_repository import get_current_user_id
from app.domain.schemas import DeviceBase
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

    class GetDevicesResDevice(DeviceBase):
        item: str
        weight: int
        percentage: float
        color: Optional[str]
        expiration_date: Optional[str]

    class GetDevicesRes(BaseModel):
        devices: List[GetDevicesResDevice]

    @router.get("/devices", response_model=GetDevicesRes)
    def get_states(
            ssn: Session = Depends(db.get_db),
            user_id: str = Depends(get_current_user_id),
    ):
        try:
            devices = repository.get_devices_by_user_id(ssn, user_id)
        except Exception as err:
            traceback.print_exc()
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail='Error: %s' % err,
            )
        res_devices: List[GetDevicesResDevice] = []
        for d in devices:
            weight = d.weight or 0
            exp = d.expiration_date.isoformat() if d.expiration_date is not None else None
            try:
                percentage = 100 * (weight - d.min) / (d.max - d.min)
            except ZeroDivisionError:
                percentage = 0
            res_devices.append(GetDevicesResDevice(
                id=d.id,
                item=d.item,
                weight=weight,
                percentage=percentage,
                color=d.color,
                expiration_date=exp
            ))
        return GetDevicesRes(devices=res_devices)

    class PostDevicesReq(BaseModel):
        device_id: str
        item: str
        max: int
        min: int
        color: str
        expiration_date: str  # ISO8601

    @router.post("/devices", status_code=status.HTTP_201_CREATED)
    def post_devices(
            req: PostDevicesReq,
            ssn: Session = Depends(db.get_db),
            user_id: str = Depends(get_current_user_id),
    ):
        # すでに存在するデバイスか確認
        device = repository.get_devices_by_id(ssn, req.device_id)
        color = req.color or "#FFFFFF"
        expiration_date = req.expiration_date or None

        try:
            if device is None:
                repository.create_device(
                    ssn,
                    DeviceCreate(
                        id=req.device_id,
                        item=req.item,
                        max=req.max,
                        min=req.min,
                        color=color,
                        expiration_date=expiration_date,
                        user_id=user_id,
                    ),
                )
            else:
                repository.update_device(
                    ssn,
                    DeviceUpdate(
                        id=req.device_id,
                        item=req.item,
                        max=req.max,
                        min=req.min,
                        color=color,
                        expiration_date=expiration_date,
                        user_id=user_id,
                    )
                )
            return {}
        except ValueError as err:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='%s' % err
            )
        except Exception as err:
            traceback.print_exc()
            raise HTTPException(
                status_code=500,
                detail='Error: %s' % err,
            )

    class SearchItemResItem(BaseModel):
        name: str
        imageUrl: str
        itemUrl: str

    class SearchItemRes(BaseModel):
        items: List[SearchItemResItem]

    @router.get("/searchitem", response_model=SearchItemRes)
    def get_states(query: str):
        url = "https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706"
        appid = "1016875581354618617"
        res = requests.get(url, params={"format": "json", "keyword": query, "applicationId": appid}).json()
        res_items: List[SearchItemRes] = []
        try:
            for item in res['Items']:
                res_items.append(SearchItemResItem(
                    name=item['Item']['itemName'],
                    imageUrl=item['Item']['mediumImageUrls'][0]['imageUrl'],
                    itemUrl=item['Item']['itemUrl']
                ))
        except Exception as err:
            traceback.print_exc()
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail='Error: %s' % err,
            )
        return SearchItemRes(items=res_items)

    return router
