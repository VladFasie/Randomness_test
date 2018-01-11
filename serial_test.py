from math import log2, pow
from utils import bit, intToStrBin, count_all
from test import Test
from scipy.special import gammaincc

class Serial(Test):

    def __init__(self, m=3):
        self.m = m

    def test(self, int_list):
        if not self.m >= 3:
            raise AssertionError()
        n = len(int_list) * 32
        if not self.m < int(log2(n)) - 2:
            raise AssertionError()
        v0 = [0 for i in range(int(pow(2, self.m)))]
        v1 = [0 for i in range(int(pow(2, self.m - 1)))]
        v2 = [0 for i in range(int(pow(2, self.m - 2)))]

        bits = ''
        for num in int_list:
            for j in range(32):
                bits += str(bit(num, j))

        bits0 = bits + bits[0 : self.m - 1]
        bits1 = bits + bits[0 : self.m - 2]
        bits2 = bits + bits[0 : self.m - 3]

        fi0 = fi1 = fi2 = 0

        for i in range(len(v0)):
            fi0 += pow(count_all(bits0, intToStrBin(i, self.m)), 2)
        for i in range(len(v1)):
            fi1 += pow(count_all(bits1, intToStrBin(i, self.m - 1)), 2)
        for i in range(len(v2)):
            fi2 += pow(count_all(bits2, intToStrBin(i, self.m - 2)), 2)

        fi0 = (pow(2, self.m) / n) * fi0 - n
        fi1 = (pow(2, self.m - 1) / n) * fi1 - n
        fi2 = (pow(2, self.m - 2) / n) * fi2 - n

        d1 = fi0 - fi1
        d2 = fi0 - 2 * fi1 + fi2

        p_val1 = gammaincc(pow(2, self.m - 2), d1)
        p_val2 = gammaincc(pow(2, self.m - 3), d2)

        return p_val1 >= 0.01 and p_val2 >= 0.01
