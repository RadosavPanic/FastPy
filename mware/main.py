from fastapi import FastAPI, Request
import time
from pydantic import BaseModel
from mware.db import engine, SessionLocal
from mware.models import Base, Item

app = FastAPI()

Base.metadata.create_all(bind=engine)

class ItemSchema(BaseModel):
    name: str
    quantity: int
    price: float

@app.middleware("http")
async def log_request_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    print(f"Request: {request.method} {request.url} completed in {process_time:.4f} seconds")
    return response

@app.get("/items/")
def get_items():
    db = SessionLocal()
    items = db.query(Item).all()
    db.close()
    return items

@app.get("/items/{item_id}")
def get_item(item_id: int):
    db = SessionLocal()
    item = db.query(Item).filter(Item.id == item_id).first()
    db.close()
    if not item:
        return {"error": "Item not found"}
    return item

@app.post("/items/")
def create_item(item: ItemSchema):
    db = SessionLocal()
    db_item = Item(name=item.name, quantity=item.quantity, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item

@app.put("/items/{item_id}")
def update_item(item_id: int, item: ItemSchema):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        db.close()
        return {"error": "Item not found"}
    db_item.name = item.name
    db_item.quantity = item.quantity
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    db.close()
    return db_item
    
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    db = SessionLocal()
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if not db_item:
        db.close()
        return {"error": "Item not found"}
    db.delete(db_item)
    db.commit()
    db.close()
    return {"message": "Item deleted successfully"}