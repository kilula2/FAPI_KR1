from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pathlib import Path

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    path = Path("index.html")
    with open(path, "r", encoding="utf-8") as f:
        html_content = f.read()
    return html_content