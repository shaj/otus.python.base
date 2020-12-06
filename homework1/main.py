#!/bin/env python3
# -*- coding: utf-8 -*-

import math
from pprint import pprint


def my_pow(data, p=2):
    retlist = []
    for item in data:
        retlist.append(item ** p)
    return retlist


def is_prime(n):
    '''
    Отсюда:
    https://stackoverflow.com/a/18833870
    '''
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def my_filter(data, f=0):
    retlist = []
    if(f == 0):
        # Even numbers
        for item in data:
            if(not (item & 1)):
                retlist.append(item)
    elif(f == 1):
        # Odd numbers
        for item in data:
            if(item & 1):
                retlist.append(item)
    elif(f == 2):
        # Prime numbers
        for item in data:
            if(is_prime(item)):
                retlist.append(item)
    return retlist


if __name__ == '__main__':
    test1 = [1, 2, 3, 4, 5]
    pprint(my_pow(test1))
    pprint(my_filter(test1))
    pprint(my_filter(test1, f=1))
    pprint(my_filter(list(range(100)), f=2))
