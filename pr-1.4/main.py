from models import User
from fastapi import FastAPI

app = FastAPI()

user = User(name="Игорь Левакин", id=1)

@app.get("/users")
async def users():
    return {"name": user.name, "id": user.id}
