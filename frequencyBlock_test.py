from math import pow
from utils import bit
from test import Test
from scipy.special import gammaincc


class FrequencyBlock(Test):

    def __init__(self, M):
        self.M = M

    def test(self, int_list):
        n = len(int_list) * 32
        N = int(n / self.M)
        if not n >= 100 or not self.M > 20 or not self.M > 0.01 * n or not N < 100:
            raise AssertionError()
        ind_int = 0
        ind_bit = 0
        chi_sq = 0.0
        for i in range(N):
            sp = 0
            for j in range(self.M):
                sp += bit(int_list[ind_int], ind_bit)
                ind_bit += 1
                if ind_bit >= 32:
                    ind_bit = 0
                    ind_int += 1
            chi_sq += pow((sp / self.M) - 0.5, 2)
        chi_sq *= 4 * self.M
        p_val = gammaincc(N / 2, chi_sq / 2)
        return p_val >= 0.01
