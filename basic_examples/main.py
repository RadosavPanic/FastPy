from fastapi import FastAPI
from item import Item, ItemResponse

app = FastAPI()

items: list[Item] = []

@app.get("/")
def read_root():
    return "Welcome to FastAPI"

@app.get("/items")
def read_item():
    itemStr = ""
    for index, item in enumerate(items):
        itemStr += f"Item {index}: {item.name}, Price: {item.price}, Is Offer: {item.is_offer}\n"        
    return itemStr

@app.post("/items/", response_model=ItemResponse)
def create_item(item: Item):
    items.append(item)    
    return item