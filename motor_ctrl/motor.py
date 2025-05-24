import os
import serial
from enum import Enum
from time import sleep


class stepper(Enum):
    RIGHT = 0
    LEFT = 1


class sonic_sensor_pos(Enum):
    FRONT = 0
    LEFT = 1
    BACK = 2
    RIGHT = 3


class controller:

    def __init__(self, device: str):
        self.device = device
        self.serial = serial.Serial(device)
        self.speed_left = 0
        self.speed_right = 0
        self.sonic_sensors: dict[sonic_sensor_pos, int] = {}

        self.__push_speed()

    def __push_int16(buffer: list[int], speed: int):
        print("push buffer")
        print(speed)
        buffer.append(speed & 0xFF)
        buffer.append((speed & 0xFF00) >> 8)

    def __pull_int16(buffer: list[int]) -> int:
        value = 0

        value = buffer[0]
        value |= buffer[1] << 8

        return value

    def __push_speed(self):
        buffer: list[int] = []

        # header
        buffer.append(0xAA)

        controller.__push_int16(buffer, self.speed_right)
        controller.__push_int16(buffer, self.speed_left)

        buffer.append(0x0A)
        print(bytes(buffer))
        self.serial.write(bytes(buffer))
        self.serial.flush()

    def set_motor_speed(self, left_speed_float: float, right_speed_float: float):
        self.speed_left = int(left_speed_float * 4000)
        self.speed_right = int(right_speed_float * 4000)

        self.__push_speed()


# c = controller("/dev/ttyACM0")
# c.set_motor_speed(stepper.LEFT, -1)
# c.set_motor_speed(stepper.RIGHT, 1)
# while True:
#     c.handle_rx()
#     print(c.sonic_sensors)
#     sleep(0.01)
