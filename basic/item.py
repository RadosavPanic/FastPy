from pydantic import BaseModel

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = False
    password: str = 'examplepass512'
    
class ItemResponse(BaseModel):
    name: str
    price: int
    is_offer: bool = False