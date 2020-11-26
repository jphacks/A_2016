from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from firebase_admin import auth
from firebase_admin.auth import InvalidIdTokenError, UserNotFoundError, UserRecord
from starlette import status

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user_id(token: str = Depends(oauth2_scheme)):
    try:
        decoded_token = auth.verify_id_token(token)
    except InvalidIdTokenError as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='invalid token'
        )
    uid = decoded_token['uid']
    return uid


def get_user(user_id: str) -> UserRecord:
    return auth.get_user(user_id)
