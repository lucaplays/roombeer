from typing import Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

class Direction(Enum):
    FORWARD = 1,
    RIGHT = 2,
    BACK = 3,
    LEFT = 4,

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
def read_root():
    return {"Hello": "World"}

class MoveItem(BaseModel):
    direction: Direction
    is_down: bool

@app.post("/move/")
def move(move_item: MoveItem):
    return {"req": "moved"}