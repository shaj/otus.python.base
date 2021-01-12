# -*- coding: utf-8 -*-

from .vehicle import Vehicle
from .vehiclemixin import CarradioMixin, NavigatorMixin
from enum import Enum, unique


class DirectionError(Exception):
    pass


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

    __accel_to_speed = {
        Accel.DUAL_FOLLOW_BACK: -120,
        Accel.FOLLOW_BACK: -75,
        Accel.NON_FOLLOW_BACK: -25,
        Accel.STOP: 0,
        Accel.NON_FOLLOW_UP: 25,
        Accel.FOLLOW_UP: 75,
        Accel.DUAL_FOLLOW_UP: 120
    }

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
        return self.__accel_to_speed[self._speed] * self._max_speed / 100


class NewBoat(NavigatorMixin, Boat):
    """ """

    def __init__(self, name="Пароходик", max_speed=50):
        super().__init__(name, max_speed)


class SailBoat(CarradioMixin, NavigatorMixin, Boat):
    """docstring for SailBoat"""

    def __init__(self, name="Беда", max_speed=50):
        super().__init__(name, max_speed)

    def accelerate(self, n: int):
        if n > 0:
            if self._speed != Boat.Accel.DUAL_FOLLOW_UP:
                self._speed = Boat.Accel(self._speed.value + 1)
        elif n < 0:
            raise DirectionError('Only positive acceleration is possible')
        else:
            self._speed = Boat.Accel.STOP

