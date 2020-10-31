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
