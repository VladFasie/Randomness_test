from utils import bit
from test import Test
from math import sqrt, pow, log2
from scipy.special import erfc


class Maurer(Test):

    def __init__(self, L, Q):
        if not L >= 6:
            raise AssertionError()
        self.Q = Q
        self.L = L
        self.E = [
            [5.2177052, 2.954],
            [6.1962507, 3.125],
            [7.1836656, 3.238],
            [8.1764248, 3.311],
            [9.1723243, 3.356],
            [10.170032, 3.384],
            [11.168765, 3.401],
            [12.168070, 3.410],
            [13.167693, 3.416],
            [14.167488, 3.419],
            [15.167379, 3.421]
        ]

    def test(self, int_list):
        T = [0 for i in range(int(pow(2, self.L)))]
        blocks = []
        n = len(int_list) * 32
        blocks_num = int(n / self.L)
        ind_int = 0
        ind_bit = 0
        for i in range(blocks_num):
            val = 0
            for j in range(self.L):
                val += bit(int_list[ind_int], ind_bit) * int(pow(2, self.L - j - 1))
                ind_bit += 1
                if ind_bit >= 32:
                    ind_bit = 0
                    ind_int += 1
            blocks.append(val)
        for i in range(self.Q):
            T[blocks[i]] = i + 1
        fn = 0.0
        for i in range(self.Q, blocks_num):
            tmp = i + 1 - T[blocks[i]]
            T[blocks[i]] = i + 1
            fn += log2(tmp)
        K = blocks_num - self.Q
        fn /= K
        c = 0.7 - 0.8 / self.L + (4 + 32.0 / self.L) * (pow(K, -3.0 / self.L) / 15)
        sgm = c * sqrt(1.0 * self.E[self.L - 6][1] / (blocks_num - self.Q))
        p_val = erfc(abs((fn - self.E[self.L - 6][0]) / (sqrt(2) * sgm)))
        return p_val >= 0.01
