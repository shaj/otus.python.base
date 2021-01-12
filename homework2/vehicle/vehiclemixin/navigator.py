# -*- coding: utf-8 -*-


class NavigatorMixin:
    """ """

    # def __init__(self):
    #     super().__init__()

    def navigator_on(self):
        print('Navigator ON')

    def navigator_off(self):
        print('Navigator OFF')

    def navigator_set_start_point(self, pt):
        print(f'Start point {pt}')

    def navigator_set_end_point(self, pt):
        print(f'End point {pt}')

    def navigator_get_route(self):
        print('Route')
