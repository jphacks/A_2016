import os

from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import App
from starlette.middleware.cors import CORSMiddleware

from .db import Database
from .firebase import admin
from .router import v1, v2


def new_app(db: Database, firebase_app: App) -> FastAPI:
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
    a.include_router(v2.new_router(db), prefix="/v2")
    return a


DATABASE_URL = os.environ.get("DATABASE_URL", "")

app = new_app(
    Database(DATABASE_URL),
    admin.new_app(),
)
