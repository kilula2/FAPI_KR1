from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name: str
    age: int

def is_adult(n):
    return n>=18

@app.post("/user")
async def uwuser(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "is_adult": is_adult(user.age)
    }