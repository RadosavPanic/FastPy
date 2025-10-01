from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from fastapi.requests import Request

app = FastAPI()

class NotFoundException(Exception):
    def __init__(self, name: str):
        self.name = name
            
@app.exception_handler(NotFoundException)
def not_found_exception_handler(request: Request, exc: NotFoundException):
    return JSONResponse(
        status_code=404,
        content={"message": f"Oops! {exc.name} not found"}
    )
    
items = {'apple': 10, 'banana': 20, 'orange': 30}

@app.get("/items/{item_name}")
def get_item(item_name: str):
    if item_name not in items:
        raise NotFoundException(item_name)
    return {"item": item_name, "price": items[item_name]}