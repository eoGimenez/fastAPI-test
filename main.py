from fastapi import FastAPI
from routes import users, auth, jwt_auth


app = FastAPI()

app.include_router(users.router)
app.include_router(auth.router)
app.include_router(jwt_auth.router)


@app.get("/")
async def root():
    return {"message": "Buenas! desde main"}
