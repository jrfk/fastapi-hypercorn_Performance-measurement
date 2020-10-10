from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import asyncio

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/query")
async def hello_query(id: str = None):
    return {"text": f"spam, egg, spam and spam!, {id}!"}

@app.get("/message/{id}")
async def get_message(id:str):
    await asyncio.sleep(3)
    return {"text": f"spam, egg, spam and spam!, {id}!"}

