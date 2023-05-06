import os
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt
from passlib.context import CryptContext

hash_sys = "HS256"
token_life = 1
SECRET = os.environ.get("SECRET")
router = APIRouter()

auth_sys = OAuth2PasswordBearer(tokenUrl="login")

bcrypt = CryptContext(schemes=["bcrypt"])


class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "euge": {
        "username": "euge",
        "full_name": "Euge Gime",
        "email": "a@a.com",
        "disabled": False,
        "password": "$2a$12$1iv4kG0cOvnePZMIvrcfhuCi1Q3K/ha/oMtLoiAYvqWrlCt2CbBOm"
    },
    "euge2": {
        "username": "euge2",
        "full_name": "Euge Gime",
        "email": "a22@a.com",
        "disabled": True,
        "password": "$2a$12$llVCfpLpXuWgt2L7TGZ6c.HaZhABykIE9ubsKZ3Olr0dtr6Mq921u"
    }
}


def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])
    raise HTTPException(status_code=401,
                        detail="Credenciales incorrectas - PASS FUNCION",
                        headers={"WWW-authenticate": "Bearer"})


@router.post("/jwt")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="Credenciales incorrectas - USER")
    user = search_user(form.username)
    if not bcrypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=400, detail="Credenciales icorrectas - PASS FORM")
    access_token = {"usr": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=token_life)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=hash_sys), "token_type": "bearer"}
