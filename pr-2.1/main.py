from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

fbs = []

@app.post("/feedback")
async def feeb(fb: Feedback):
    fbs.append(fb)
    return {"message": f"Feedback received. Thank you, {fb.name}."}