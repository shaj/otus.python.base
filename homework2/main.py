#!/bin/env pyton3
# -*- coding: utf-8 -*-

from vehicle import Vehicle, Car, Boat
from vehicle.boat import DirectionError
from vehicle.vehiclemixin import CarradioMixin


def test_drive(vh: Vehicle):
    if not isinstance(vh, Vehicle):
        raise ValueError("vh must be derived from Vehicle")
    print('Test drive of a "{}" called "{}"'.format(vh.__class__.__name__, vh.name))
    try:
        vh.beep()
        if vh.current_speed != 0:
            vh.slow_down(abs(vh.current_speed))
        vh.accelerate(60)
        vh.accelerate(60)
        print(vh.current_speed)
        vh.slow_down(60)
        vh.slow_down(60)
        print(vh.current_speed)
        vh.accelerate(-60)
        vh.accelerate(-60)
        print(vh.current_speed)
        vh.slow_down(60)
        vh.slow_down(60)
        print(vh.current_speed)
        vh.beep()
    except Exception as e:
        print('Error in test_drive({}): "{}"'.format(vh, e.args[0]))


def vehicle_interface_test(vh: Vehicle):
    pass


class Bicycle(CarradioMixin, Vehicle):
    """ """

    def __init__(self, name="Орлёнок", max_speed=15):
        super().__init__(name, max_speed)

    def accelerate(self, n: int):
        if n < 0:
            raise DirectionError('Only positive acceleration is possible')

    def slow_down(self, n: int):
        pass

    def beep(self):
        print('Ding...')


if __name__ == '__main__':
    my_car = Car("Packard", 100)
    test_drive(my_car)
    my_boat = Boat("Meteor", 20)
    test_drive(my_boat)
    my_bi = Bicycle()
    test_drive(my_bi)
    try:
        test_drive("string")
    except Exception as e:
        print('Error in test_drive(): "{}"'.format(e.args[0]))
