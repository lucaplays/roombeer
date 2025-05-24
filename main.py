from typing import Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel
from motor_ctrl.motor import controller, stepper

from fastapi.middleware.cors import CORSMiddleware

stepper = controller(device="/dev/ttyACM0")

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
    is_down: bool = Field(..., alias="isDown")


@app.post("/move/")
def move(move_item: MoveItem):
    on_off = int(move_item.is_down);
    
    match move_item.direction:
        case Direction.FORWARD:
            stepper.set_motor_speed(stepper.LEFT, on_off)
            stepper.set_motor_speed(stepper.RIGHT, on_off)
        case Direction.RIGHT:
            stepper.set_motor_speed(stepper.LEFT, on_off)
        case Direction.BACK:
            stepper.set_motor_speed(stepper.LEFT, -on_off)
            stepper.set_motor_speed(stepper.RIGHT, -on_off)
        case Direction.LEFT:
            stepper.set_motor_speed(stepper.RIGHT, on_off)
            
    return {"req": "moved", "parsed": move_item}
