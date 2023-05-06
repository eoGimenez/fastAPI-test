from fastapi import FastAPI
from routes import users


app = FastAPI()

app.include_router(users.router)


@app.get("/")
async def root():
    return {"message": "Buenas! desde main"}
