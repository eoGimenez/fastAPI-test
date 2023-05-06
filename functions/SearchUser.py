def search_user(id: int, db):
    user = filter(lambda user: user.id == id, db)
    try:
        return list(user)[0]
    except:
        return {"message": "El usuario no existe"}
