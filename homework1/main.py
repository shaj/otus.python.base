#!/bin/env python3
# -*- coding: utf-8 -*-

import math
import operator
from pprint import pprint
import time
from functools import wraps


def my_timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time.clock()
        ret = func(*args, **kwargs)
        print(func.__name__, time.clock() - t)
        return ret
    return wrapper


def my_depth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        ret = func(*args, **kwargs)
        if wrapper.maxdepth < wrapper.count:
            wrapper.maxdepth = wrapper.count
        wrapper.count -= 1
        if wrapper.count == 0:
            print(u"Глубина вызовов {0} была {1}".format(func.__name__, wrapper.maxdepth))
            wrapper.maxdepth = 0
        return ret
    wrapper.count = 0
    wrapper.maxdepth = 0
    return wrapper


def my_pow(data, p=2):
    return list(map(lambda x: x ** p, data))


def my_pow1(data, p=2):
    list_pow = [p] * len(data)
    return list(map(operator.pow, data, list_pow))


def is_prime(n):
    '''
    Отсюда:
    https://stackoverflow.com/a/18833870
    '''
    if n < 0:
        return False
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


FILTER_EVEN_NUMBERS = 0
FILTER_ODD_NUMBERS = 1
FILTER_PRIME_NUMBERS = 2


def my_filter(data, f=0):
    if f == FILTER_EVEN_NUMBERS:
        # Even numbers
        return list(filter(lambda x: not (x & 1), data))
    if f == FILTER_ODD_NUMBERS:
        # Odd numbers
        return list(filter(lambda x: x & 1, data))
    if f == FILTER_PRIME_NUMBERS:
        # Prime numbers
        return list(filter(is_prime, data))
    # Unknown command
    return list()


@my_depth
def fyb(n):
    if n == 0:
        return 0
    if n <= 2:
        return 1
    return fyb(n - 1) + fyb(n - 2)


@my_timeit
def fybonacci(n):
    return fyb(n)


if __name__ == '__main__':
    test1 = [1, 2, 3, 4, 5]
    pprint(my_pow(test1))
    pprint(my_pow(test1, p=0.5))
    pprint(my_pow1(test1))
    pprint(my_pow1(test1, p=0.5))
    pprint(my_filter(test1))
    pprint(my_filter(test1, f=FILTER_EVEN_NUMBERS))
    pprint(my_filter(test1, f=FILTER_ODD_NUMBERS))
    pprint(my_filter(list(range(100)), f=FILTER_PRIME_NUMBERS), compact=True)
    pprint(my_filter([-1, -2, -3, -4, -5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], f=FILTER_PRIME_NUMBERS),
           compact=True)

    print('\nИсследование декораторов:\n')
    print(fybonacci(10))
    print(fybonacci(11))
    print(fybonacci(20))
