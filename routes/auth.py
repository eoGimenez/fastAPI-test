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
        return UserDB(**users_db[username])
    raise HTTPException(status_code=401,
                        detail="Credenciales incorrectas - PASS FUNCION",
                        headers={"WWW-authenticate": "Bearer"})


def search_user_protected(username: str):
    if username in users_db:
        return User(**users_db[username])
    raise HTTPException(status_code=401,
                        detail="Credenciales incorrectas - PROTECTED FUNCION",
                        headers={"WWW-authenticate": "Bearer"})


async def current_user(token: str = Depends(auth_sys)):
    user = search_user_protected(token)
    if not user:
        raise HTTPException(status_code=401,
                            detail="Credenciales incorrectas - ASYNC FUNCION",
                            headers={"WWW-authenticate": "Bearer"})
    if user.disabled:
        raise HTTPException(status_code=400,
                            detail="usuario inactivo, contacte con soporte")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=400, detail="Credenciales incorrectas - USER")
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=400, detail="Credenciales icorrectas - PASS FORM")
    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/profile")
async def profile(user: User = Depends(current_user)):
    return user
