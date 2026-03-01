from fastapi import FastAPI

pens = FastAPI()

@pens.get("/")
async def root():
    return {"message": "Авторелоад действительно работает"}