import random
from datetime import datetime


def chi_square(intended_vector, value_expected):
    x_square = 0
    for i in range(10):
        s_value = intended_vector[i] - value_expected
        x_square = x_square + (s_value * s_value) / value_expected

    print(f"chi_square: {x_square}")
    return 0


class MLCG(object):
    def __init__(self):
        self._m = 4930622455819
        self._a = 2106408

    def get_random_number(self, range_value, module_range=10):
        random.seed(datetime.now())
        x = random.random() % self._m
        for i in range(range_value):
            x = (self._a * x) % self._m

        return x % module_range
