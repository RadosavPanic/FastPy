from fastapi import FastAPI, Request, UploadFile, File
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os
import shutil

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_DIR = os.path.join(BASE_DIR, "static", "uploads")

os.makedirs(UPLOAD_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=os.path.join(BASE_DIR, "static")), name="static")
templates = Jinja2Templates(directory="images/templates")

@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    return templates.TemplateResponse("form.html", {"request": request})

@app.post("/upload", response_class=HTMLResponse)
async def upload_image(request: Request, file: UploadFile = File(...)):
    file_location = os.path.join(UPLOAD_DIR, file.filename)
    with open(file_location, "wb") as f:
        shutil.copyfileobj(file.file, f)
        
    file_info = {
        'filename': file.filename,
        'content_type': file.content_type,
        'image_url': f"/static/uploads/{file.filename}"
    }
    
    return templates.TemplateResponse("result_image.html", {
        'request': request,
        'file_info': file_info
    })