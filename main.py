from typing import Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, Field
from motor_ctrl.motor import controller, stepper

from fastapi.middleware.cors import CORSMiddleware

ctrler = controller(device="/dev/ttyACM0")

class Direction(int, Enum):
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
    is_down: bool = Field(..., alias="isDown")


@app.post("/move/")
def move(move_item: MoveItem):
    on_off = int(move_item.is_down) * 0.6;
    
    match move_item.direction:
        case Direction.FORWARD:
            ctrler.set_motor_speed(on_off, on_off)
        case Direction.RIGHT:
            ctrler.set_motor_speed(on_off, 0)
        case Direction.BACK:
            ctrler.set_motor_speed(-on_off, -on_off)
        case Direction.LEFT:
            ctrler.set_motor_speed(0, on_off)
            
    return {"req": "moved", "parsed": move_item}
