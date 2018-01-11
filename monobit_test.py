from utils import bit
from test import Test
from math import sqrt
from scipy.special import erfc


class MonoBit(Test):

    def test(self, int_list):
        s = 0
        for num in int_list:
            for i in range(32):
                s += 2 * bit(num, i) - 1
        s_obs = abs(s) / sqrt(len(int_list) * 32)
        p_val = erfc(s_obs / sqrt(2))
        return p_val >= 0.01
