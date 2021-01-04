#!/bin/env pyton3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod


class Vehicle(ABC):
    """ """

    def __init__(self, name="", max_speed=0):
        super().__init__()
        self.name = name
        self._speed = 0
        self._max_speed = max_speed

    @abstractmethod
    def accelerate(self, n: int):
        pass

    @abstractmethod
    def slow_down(self, n: int):
        pass

    @abstractmethod
    def beep(self):
        pass

    @property
    def current_speed(self):
        return self._speed

    @property
    def max_speed(self):
        return self._max_speed
