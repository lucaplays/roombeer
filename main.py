import asyncio

from typing import Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, Field
from motor_ctrl.motor import controller, stepper, sonic_sensor_pos

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


async def main():
    while True:
        ctrler.handle_rx()
        await asyncio.sleep(0.01)


@app.on_event("startup")
async def startup_event():
    asyncio.create_task(main())


@app.get("/")
def read_root():
    return {"Hello": "World"}


class sonicDistanceItem:
    direction: Direction
    distance: int

    def __init__(self, direction: Direction, distance: int):
        self.direction = direction
        self.distance = distance

    def toMap(self):
        return {
            "direction": self.direction,
            "distance": self.distance,
        }


@app.get("/sonicdistance/")
def sonic_distance():
    return {
        "res": [
            sonicDistanceItem(
                direction=Direction.FORWARD, distance=ctrler.sonic_sensors[sonic_sensor_pos.FRONT.value]
            ).toMap(),
            sonicDistanceItem(
                direction=Direction.RIGHT, distance=ctrler.sonic_sensors[sonic_sensor_pos.RIGHT.value]
            ).toMap(),
            sonicDistanceItem(
                direction=Direction.BACK, distance=ctrler.sonic_sensors[sonic_sensor_pos.BACK.value]
            ).toMap(),
            sonicDistanceItem(
                direction=Direction.LEFT, distance=ctrler.sonic_sensors[sonic_sensor_pos.LEFT.value]
            ).toMap(),
        ]
    }


class MoveItem(BaseModel):
    direction: Direction
    is_down: bool = Field(..., alias="isDown")


@app.post("/move/")
def move(move_item: MoveItem):

    on_off = int(move_item.is_down) * 0.1;
    match move_item.direction:
        case Direction.FORWARD:
            ctrler.set_motor_speed(on_off, on_off)
        case Direction.RIGHT:
            ctrler.set_motor_speed(on_off, -on_off)
        case Direction.BACK:
            ctrler.set_motor_speed(-on_off, -on_off)
        case Direction.LEFT:
            ctrler.set_motor_speed(-on_off, on_off)
            

    return {"req": "moved", "parsed": move_item}

#SPEED CONTROL
@app.post("/speed/")
def move(speed: float):
    ctrler.speed_left = speed
    ctrler.speed_right = speed
    return {"req": "speed", "parsed": speed}