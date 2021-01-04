#!/bin/env pyton3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class BaseVehicle(ABC):
    """docstring for BaseVehicle"""

    def __init__(self, arg):
        super(BaseVehicle, self).__init__()
        self.arg = arg

    @abstractmethod
    def function(self):
        pass


class Car(BaseVehicle):
    """docstring for Car"""

    def __init__(self, arg):
        super(Car, self).__init__(arg)
        self.arg = arg

    def function(self, a):
        self.a = a


class Bot(BaseVehicle):
    """docstring for Bot"""

    def __init__(self, arg):
        super(Bot, self).__init__(arg)
        self.arg = arg

    def function(self, a):
        self.a = a


a = Car('base')
b = Bot('start')
