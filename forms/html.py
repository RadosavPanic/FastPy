from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=BASE_DIR / "templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/submit", response_class=HTMLResponse)
def submit_form(request: Request, username: str = Form(...), freq: int = Form(...)):
    context = {
        "request": request,
        "username": username,
        "freq": freq
    }
    return templates.TemplateResponse("result.html", context)