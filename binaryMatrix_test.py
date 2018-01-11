from numpy.linalg import matrix_rank
from math import pow, exp
from utils import bit
from test import Test
from scipy.special import gammaincc


class BinaryMatrix(Test):

    def __init__(self):
        self.M = self.Q = 32

    def test(self, int_list):
        n = len(int_list) * 32
        if not n >= 38 * self.M * self.Q:
            raise AssertionError()
        r = [0.0, 0.0, 0.0]
        ind_int = 0
        matrix_num = int(n / (self.M * self.Q))
        for i in range(matrix_num):
            m = []
            for j in range(self.M):
                l = []
                for k in range(self.Q):
                    l.append(bit(int_list[ind_int], k))
                ind_int += 1
                m.append(l)
            rank = matrix_rank(m)
            if rank == self.M:
                r[0] += 1
            elif rank == self.M - 1:
                r[1] += 1
        r[2] = matrix_num - r[0] - r[1]
        chi_sq = (pow((r[0] - 0.2888 * matrix_num), 2) / (0.2888 * matrix_num))
        chi_sq += (pow((r[1] - 0.5776 * matrix_num), 2) / (0.5776 * matrix_num))
        chi_sq += (pow((r[2] - 0.1336 * matrix_num), 2) / (0.1336 * matrix_num))
        #p_val = exp(-chi_sq / 2)
        p_val = gammaincc(1.0, chi_sq / 2)
        return p_val >= 0.01
