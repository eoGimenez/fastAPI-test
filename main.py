from typing import List
from fastapi import FastAPI
from models.User import User


db: List[User] = [
    User(id=1, name="Euge", surname="Gime", age=38, height=1.86),
    User(id=2, name="Juli", surname="Mattos", age=29, height=1.65),
    User(id=3, name="Uno", surname="Dos", age=18, height=1.22)
]


def search_user(id: int):
    user = filter(lambda user: user.id == id, db)
    try:
        return list(user)[0]
    except:
        return {"message": "El usuario no existe"}


app = FastAPI()


@app.get('/users')
async def users():
    return db


@app.get("/users/{id}")
async def get_user(id: int):
    return search_user(id)


@app.post("/users/new")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"message": "El usuario ya exite"}
    else:
        db.append(user)
        return [{"message": "EL usuario ha sido creado correctamente"}, db]


@app.put("users/{id}")
async def edit_user(id: int, user: User):
    user_to_change = search_user(id)
    print("??" + user_to_change)
    user_to_change = user
    return user_to_change
