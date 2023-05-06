from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm


router = APIRouter()

auth_sys = OAuth2PasswordBearer(tokenUrl="login")


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
        "password": "asdasd"
    },
    "euge2": {
        "username": "euge2",
        "full_name": "Euge Gime",
        "email": "a22@a.com",
        "disabled": True,
        "password": "123123"
    }
}


def search_user(username: str):
    if username in users_db:
        return UserDB(users_db[username])
    return {"message": "Credenciales incorrectas"}


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=400, detail="Credenciales icorrectas")
    return {"access_token": , "token_type": "bearer"}
