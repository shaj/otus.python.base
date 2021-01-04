#!/bin/env pyton3
# -*- coding: utf-8 -*-

from vehicle import Vehicle, Car, Boat, vehiclemixin


def test_drive(vh: Vehicle):
    if not isinstance(vh, Vehicle):
        raise ValueError("vh must be derived from Vehicle")
    print('Test drive of a "{}" called "{}"'.format(vh.__class__.__name__, vh.name))
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


if __name__ == '__main__':
    my_car = Car("Packard", 100)
    test_drive(my_car)
    my_boat = Boat("Meteor", 20)
    test_drive(my_boat)
    try:
        test_drive("string")
    except Exception as e:
        print('Error in test_drive(): "{}"'.format(e.args[0]))
