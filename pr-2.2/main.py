from fastapi import FastAPI
from pydantic import BaseModel, field_validator
import re

app = FastAPI()

class Feedback(BaseModel):
    name: str
    message: str

    @field_validator('name')
    def validate_name(cls, v):
        if len(v) < 2 or len(v) > 50:
            raise ValueError('Имя должно быть от 2 до 50 символов')
        return v

    @field_validator('message')
    def validate_message(cls, v):
        if len(v) < 10 or len(v) > 500:
            raise ValueError('Сообщение должно быть от 10 до 500 символов')
        
        forbidden_words = ['кринж', 'рофл', 'вайб']
        for word in forbidden_words:
            if re.search(word, v, re.IGNORECASE):
                raise ValueError('Использование недопустимых слов')
        return v

fbs = []

@app.post("/feedback")
async def feeb(fb: Feedback):
    fbs.append(fb)
    return {"message": f"Спасибо, {fb.name}! Ваш отзыв сохранён."}
