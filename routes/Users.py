from typing import List
from fastapi import APIRouter
from models.User import User
from functions.SearchUser import search_user


db: List[User] = [
    User(id=1, name="Euge", surname="Gime", age=38, height=1.86),
    User(id=2, name="Juli", surname="Mattos", age=29, height=1.65),
    User(id=3, name="Uno", surname="Dos", age=18, height=1.22)
]


router = APIRouter(prefix="/users", tags=["Users"])


@router.get('/')
async def users():
    return db


@router.get("/{id}")
async def get_user(id: int):
    return search_user(id, db)


@router.post("/")
async def create_user(user: User):
    if type(search_user(user.id, db)) == User:
        return {"message": "El usuario ya exite"}
    else:
        db.append(user)
        return [{"message": "EL usuario ha sido creado correctamente"}, db]


@router.put("/")
async def edit_user(user: User):
    for index, db_user in enumerate(db):
        if db_user.id == user.id:
            db[index] = user
            return [{"message": "EL usuario ha sido actualizado correctamente"}, db]
    return {"message": "El usuario no existe"}


@router.delete("/{id}")
async def delete_user(id: int):
    for index, db_user in enumerate(db):
        if db_user.id == id:
            del db[index]
            return [{"message": "EL usuario ha sido eliminado"}, db]
    return {"message": "El usuario no existe"}
