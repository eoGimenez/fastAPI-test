from typing import List
from fastapi import APIRouter
from models.User import User
from functions.SearchUser import search_user, search_user_by_surname
from db.config import db
from schemas.user import user_schema, users_schema

db__: List[User] = [
    """  User(id=1, name="Euge", surname="Gime", age=38, height=1.86),
    User(id=2, name="Juli", surname="Mattos", age=29, height=1.65),
    User(id=3, name="Uno", surname="Dos", age=18, height=1.22) """
]


router = APIRouter(prefix="/users", tags=["Users"])


@router.get('/')
async def users():
    return users_schema(db.fastAPI.users.find())


@router.get("/{id}")
async def get_user(id: str):
    return search_user(id)


@router.post("/")
async def create_user(user: User):
    # if type(search_user(user.id, db)) == User:
    #     return {"message": "El usuario ya exite"}
    # db.append(user) esto es offline
    if type(search_user_by_surname(user.surname)) == User:
        return {"message": "El usuario ya exite"}

    new_id = db.fastAPI.users.insert_one(dict(user)).inserted_id
    return [{"message": "EL usuario ha sido creado correctamente"}, user_schema(db.fastAPI.users.find_one({"_id": new_id}))]


@router.put("/")
async def edit_user(user: User):
    for index, db_user in enumerate(users_schema(db.fastAPI.users)):
        if db_user.id == user.id:
            db[index] = user
            return [{"message": "EL usuario ha sido actualizado correctamente"}, db]
    return {"message": "El usuario no existe"}


@router.delete("/{id}")
async def delete_user(id: str):
    for index, db_user in enumerate(users_schema(db.fastAPI.users.find())):
        print(id)
        if db_user.id == id:
            del db[index]
            return [{"message": "EL usuario ha sido eliminado"}, db]
    return {"message": "El usuario no existe"}
