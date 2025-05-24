import asyncio

from typing import Union
from enum import Enum
from fastapi import FastAPI
from pydantic import BaseModel, Field
from motor_ctrl.motor import controller, stepper, sonic_sensor_pos

from fastapi.middleware.cors import CORSMiddleware

ctrler = controller(device="/dev/ttyACM0")

speed: float = 0.5

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


class SonicSensors:
    sensors: list[int]
    is_loaded: bool


@app.get("/sonicsensors/")
def sonic_sensors(sensors: SonicSensors):
    return {
        "res": {
            "sensors": sensors.sensors,
            "isLoaded": sensors.is_loaded
        }
    }

class MoveItem(BaseModel):
    direction: Direction
    is_down: bool = Field(..., alias="isDown")



@app.post("/move/")
def move(move_item: MoveItem):

    on_off = int(move_item.is_down) * speed
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

class SpeedItem(BaseModel):
    speed: float

#SPEED CONTROL
@app.post("/speed/")
def move(item: SpeedItem):
    global speed
    speed = item.speed    
    return {"req": item}