# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass
class Vehicle(ABC):
    """ """

    name: str = ""
    _max_speed: int = 0
    _speed: int = field(init=False)

    def __post_init__(self):
        self._speed = 0

    def __str__(self):
        return 'Object "{}" named as "{}"'.format(self.__class__.__name__, self.name)

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
