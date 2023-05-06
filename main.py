from fastapi import FastAPI
from routes import Users


app = FastAPI()

app.include_router(Users.router)


@app.get("/")
async def root():
    return {"message": "Buenas! desde main"}
