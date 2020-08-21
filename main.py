from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None


app = FastAPI()


@app.post('/items/')
def create_item(item: Item):
    return item

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get('/items/{item_title}')
def read_item_title(item_title: str):
    return { 'item_title': item_title }

@app.get('/items/{item_id}')
def read_item_id(item_id: int):
    return { 'item_id': item_id }