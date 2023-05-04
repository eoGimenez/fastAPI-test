from typing import Union
from pydantic import BaseModel
from fastapi import FastAPI


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int
    height: Union[float, None] = None


hard_coded = [{"id": 1, "name": "Euge", "surname": "Gime", "age": 38,
              "height": 1.86},
              {"id": 2, "name": "Juli", "surname": "Mattos", "age": 29,
              "height": 1.65},
              {"id": 3, "name": "Uno", "surname": "Dos", "age": 18,
              "height": 1.22}]


app = FastAPI()


@app.get('/users')
async def users():
    return hard_coded


@app.get("/users/{id}")
async def get_user(id: int):
    return search_user(id)


@app.post("/users/new")
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        return {"message": "El usuario ya exite"}
    else:
        hard_coded.append(user)
        # return [{"message": "EL usuario ha sido creado correctamente"}, hard_coded]


@app.put("users/{user_id}/update")
async def edit_user(user_id: int, user: User):
    user_to_change = search_user(user_id)
    user_to_change = user
    return user_to_change


def search_user(id: int):
    user = filter(lambda user: user.id == id, hard_coded)
    try:
        return list(user)[0]
    except:
        return {"message": "El usuario no existe"}
