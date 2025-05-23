import os
from enum import Enum


class stepper(Enum):
    RIGHT = 0
    LEFT = 1


class controller:

    def __init__(self, device: str):
        self.device = device
        self.fd = os.open(device, os.O_RDWR)
        self.speed_left = 0
        self.speed_right = 0

        # self.__push_speed()

    def __push_speed(self):
        buffer: list[int] = []

        # header
        buffer.append(0xAA)

        # right motor
        buffer.append(self.speed_right & 0xFF)
        buffer.append((self.speed_right & 0xFF00) >> 8)

        # left motor
        buffer.append(self.speed_left & 0xFF)
        buffer.append((self.speed_left & 0xFF00) >> 8)

        os.write(self.fd, bytes(buffer))

    def set_motor_speed(self, ste: stepper, speed: float):
        if ste == stepper.RIGHT:
            self.speed_right = speed
        else:
            self.speed_left = speed

        self.__push_speed()


ctrl = controller("/dev/ttyACM0")
ctrl.set_motor_speed(stepper.RIGHT, 1000)
ctrl.set_motor_speed(stepper.LEFT, 200)
