from db.config import db
from schemas.user import users_schema
from models.User import User


def search_user(id: int):
    try:
        user = db.fastAPI.users.find_one({"id": id})
        return User(**users_schema(user))
    except:
        return {"message": "El usuario no existe"}
# def search_user(id: int, db):
#     user = filter(lambda user: user.id == id, db)
#     try:
#         return list(user)[0]
#     except:
#         return {"message": "El usuario no existe"}


def search_user_by_surname(surname: str):
    try:
        user = db.fastAPI.users.find_one({"surname": surname})
        return User(**users_schema(user))
    except:
        return {"message": "El usuario no existe"}
