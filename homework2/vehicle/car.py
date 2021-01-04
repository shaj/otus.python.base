#!/bin/env pyton3
# -*- coding: utf-8 -*-

from .vehicle import Vehicle


class Car(Vehicle):
    """ """

    def __init__(self, name="Ведро с болтами", max_speed=50):
        super().__init__(name, max_speed)

    def __str__(self):
        return super().__str__()

    def accelerate(self, n: int):
        if (self._speed + n) > self._max_speed:
            self._speed = self._max_speed
        elif (self._speed + n) < (-self._max_speed):
            self._speed = -self._max_speed
        else:
            self._speed += n

    def slow_down(self, n: int):
        if n < 0:
            raise ""
        if self._speed > 0:
            if n > self._speed:
                self._speed = 0
            else:
                self._speed -= n
        elif self._speed < 0:
            if n > abs(self._speed):
                self._speed = 0
            else:
                self._speed += n

    def beep(self):
        print("Beep...")

