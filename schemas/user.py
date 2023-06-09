def user_schema(user) -> dict:
    return {"id": str(user["_id"]),
            "name": user["name"],
            "surname": user["surname"],
            "age": user["age"],
            "height": user["height"]}


def users_schema(users) -> list:
    return [user_schema(user) for user in users]
