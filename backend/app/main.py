import os

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .db import Database
from .router import v1


def new_app(db: Database) -> FastAPI:
    a = FastAPI()
    cors_allow_origins = os.environ.get("CORS_ALLOW_ORIGINS", "").split(",")
    a.add_middleware(
        CORSMiddleware,
        allow_origins=cors_allow_origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    a.include_router(v1.new_router(db))
    a.include_router(v1.new_router(db), prefix="/v1")
    return a


DATABASE_URL = os.environ.get("DATABASE_URL", "")
db = Database(DATABASE_URL)

app = new_app(db)
