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
    FRONT_LEFT = 4
    FRONT_RIGHT = 5
    LOADED = 6


class controller:

    def __init__(self, device: str):
        self.device = device
        self.serial = serial.Serial(device)
        self.serial = None
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
        self.speed_left = int(left_speed_float * 1600)
        self.speed_right = int(right_speed_float * 1600)
        self.__push_speed()

    def handle_rx(self):
        buffer = self.serial.read(16)

        if buffer[0] != 0xAA:
            return

        value_cnt = buffer[1]
        for i in range(value_cnt):
            self.sonic_sensors[i] = controller.__pull_int16([buffer[2 + i * 2], buffer[2 + i * 2 + 1]]) 


# c = controller("/dev/ttyACM0")
# c.set_motor_speed(stepper.LEFT, -1)
# c.set_motor_speed(stepper.RIGHT, 1)
# while True:
#     c.handle_rx()
#     print(c.sonic_sensors)
#     sleep(0.01)
