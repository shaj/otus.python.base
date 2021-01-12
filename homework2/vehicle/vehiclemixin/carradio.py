# -*- coding: utf-8 -*-


class CarradioMixin:
    """ """

    # def __init__(self):
    #     super().__init__()
    #     self._volume = 0

    def carradio_on(self):
        print('Carradio ON')

    def carradio_off(self):
        print('Carradio OFF')

    def carradio_scan(self):
        print('Scanning of radio stations...')

    @property
    def carradio_volume(self):
        return self._volume

    @carradio_volume.setter
    def carradio_volume(self, v: int):
        print(f'Seting volume to {v}')
        self._volume = v
