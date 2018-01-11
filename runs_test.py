from math import sqrt
from utils import bit
from test import Test
from scipy.special import erfc


class Runs(Test):

    def test(self, int_list):
        n = len(int_list) * 32
        if not n >= 100:
            raise AssertionError()
        pi = 0
        for num in int_list:
            for i in range(32):
                pi += bit(num, i)
        pi /= n
        if abs(pi - 0.5) >= 2 / sqrt(n):
            return False
        v = 1
        last = None
        for num in int_list:
            for i in range(32):
                if last is not None and last != bit(num, i):
                    v += 1
                last = bit(num, i)
        val = abs(v - 2 * n * pi * (1 - pi)) / (2 * sqrt(2 * n) * pi * (1 - pi))
        p_val = erfc(val)
        return p_val >= 0.01
