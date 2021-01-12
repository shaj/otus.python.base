#!/bin/env pyton3
# -*- coding: utf-8 -*-

from vehicle import Vehicle, Car, Boat, SailBoat
from vehicle.boat import DirectionError
from vehicle.vehiclemixin import CarradioMixin, NavigatorMixin


def test_drive(vh: Vehicle):
    if not isinstance(vh, Vehicle):
        raise ValueError("vh must be derived from Vehicle")
    print('Test drive of a', vh)
    try:
        vh.beep()
        if vh.current_speed != 0:
            vh.slow_down(abs(vh.current_speed))
        vh.accelerate(60)
        vh.accelerate(60)
        print(f'After acceleration by 120 speed is {vh.current_speed}')
        vh.slow_down(60)
        vh.slow_down(60)
        print(f'After slow down by 120 speed is {vh.current_speed}')
        vh.accelerate(-60)
        vh.accelerate(-60)
        print(f'After acceleration by -120 speed is {vh.current_speed}')
        vh.slow_down(60)
        vh.slow_down(60)
        print(f'After slow down by 120 speed is {vh.current_speed}')
        vh.beep()
    except Exception as e:
        print(f'Error in test_drive <{vh}> : "{e.args[0]}"')


def vehicle_interface_test(vh: Vehicle):
    if not isinstance(vh, Vehicle):
        raise ValueError('vh must be derived from Vehicle')
    test_count = 0
    if isinstance(vh, CarradioMixin):
        vh.carradio_on()
        vh.carradio_scan()
        vh.carradio_volume = 10
        print(f'Now the carradio volume is {vh.carradio_volume}')
        vh.carradio_off()
        test_count += 1
    if isinstance(vh, NavigatorMixin):
        vh.navigator_on()
        vh.navigator_set_start_point('start')
        vh.navigator_set_end_point('end')
        vh.navigator_get_route()
        vh.navigator_off()
        test_count += 1
    if test_count == 0:
        print('Interface test: no additional equipment is installed in the vehicle')


class Bicycle(CarradioMixin, Vehicle):
    """ """

    def __init__(self, name="Орлёнок", max_speed=15):
        super().__init__(name, max_speed)

    def accelerate(self, n: int):
        if (self._speed + n) > self._max_speed:
            self._speed = self._max_speed
        elif (self._speed + n) < 0:
            raise DirectionError('Only positive speed is possible')
        else:
            self._speed += n

    def slow_down(self, n: int):
        if n < 0:
            raise ValueError('value must be positive')
        if n > self._speed:
            self._speed = 0
        else:
            self._speed -= n

    def beep(self):
        print('Ding...')


if __name__ == '__main__':

    my_car = Car("Priora", 100)
    test_drive(my_car)
    vehicle_interface_test(my_car)

    print('\n\n')
    my_boat = Boat("Meteor", 20)
    test_drive(my_boat)
    vehicle_interface_test(my_boat)

    print('\n\n')
    my_bi = Bicycle()
    test_drive(my_bi)
    vehicle_interface_test(my_bi)

    print('\n\n')
    my_sail = SailBoat()
    test_drive(my_sail)
    vehicle_interface_test(my_sail)

    print('\n\n')
    try:
        test_drive("string")
    except Exception as e:
        print('Error in test_drive(): "{}"'.format(e.args[0]))
