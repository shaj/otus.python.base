#!/bin/env pyton3
# -*- coding: utf-8 -*-

from .vehicle import Vehicle
from enum import Enum, unique


class Boat(Vehicle):
    """ """

    @unique
    class Accel(Enum):
        DUAL_FOLLOW_BACK = -3
        FOLLOW_BACK = -2
        NON_FOLLOW_BACK = -1
        STOP = 0
        NON_FOLLOW_UP = 1
        FOLLOW_UP = 2
        DUAL_FOLLOW_UP = 3

    def __init__(self, name="Дырявое корыто", max_speed=50):
        super().__init__(name, max_speed)
        self._speed: Boat.Accel = Boat.Accel.STOP

    def __str__(self):
        return super().__str__()

    def accelerate(self, n: int):
        if n > 0:
            if self._speed != Boat.Accel.DUAL_FOLLOW_UP:
                self._speed = Boat.Accel(self._speed.value + 1)
        elif n < 0:
            if self._speed != Boat.Accel.DUAL_FOLLOW_BACK:
                self._speed = Boat.Accel(self._speed.value - 1)
        else:
            self._speed = Boat.Accel.STOP

    def slow_down(self, n: int):
        self._speed = Boat.Accel.STOP

    def beep(self):
        print("Tuuuu...")

    @property
    def current_speed(self):
        return self._speed.value
