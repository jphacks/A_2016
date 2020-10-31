from typing import List

from fastapi import FastAPI
from pydantic import BaseModel
from starlette import status

app = FastAPI()


class PostStatesReq(BaseModel):
    device_id: str
    weight: int


@app.post("/states", status_code=status.HTTP_204_NO_CONTENT)
def post_states(req: PostStatesReq):
    print(req)
    return {}


class GetStatesResState(BaseModel):
    device_id: str
    item: str
    weight: int
    percentage: int


class GetStatesRes(BaseModel):
    states: List[GetStatesResState]


@app.get("/states", response_model=GetStatesRes)
def get_states():
    # TODO: replace with real data
    return {"states": [
        {
            "device_id": "5CDCD567",
            "item": "牛乳",
            "weight": 500,
            "percentage": 52
        },
        {
            "device_id": "5CDCD568",
            "item": "コーヒー牛乳",
            "weight": 500,
            "percentage": 52
        }
    ]}
