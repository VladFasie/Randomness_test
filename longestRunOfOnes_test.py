from utils import bit
from test import Test
from math import pow
from scipy.special import gammaincc

class LongestRunOfOnes(Test):

    def __init__(self):
        self.data = [
            [8, 3, 16, [0.2148, 0.3672, 0.2305, 0.1875]],
            [128, 5, 49, [0.1174, 0.2430, 0.2493, 0.1752, 0.1027, 0.1124]],
            [10000, 6, 75, [0.0882, 0.2092, 0.2483, 0.1933, 0.1208, 0.0675, 0.0727]]
        ]

    def test(self, int_list):
        n = len(int_list) * 32
        if not n >= 128:
            raise AssertionError()
        ind_data = 0
        if n >= 10000:
            ind_data = 2
        elif n >= 6272:
            ind_data = 1
        M = self.data[ind_data][0]
        K = self.data[ind_data][1]
        N = self.data[ind_data][2]
        blocks_num = int(n / M)
        ind_int = 0
        ind_bit = 0
        blocks = []
        for i in range(blocks_num):
            block = ''
            for j in range(M):
                block += str(bit(int_list[ind_int], ind_bit))
                ind_bit += 1
                if ind_bit >= 32:
                    ind_bit = 0
                    ind_int += 1
            blocks.append(block)
        v = [0 for i in range(7)]
        for block in blocks:
            ones = 0
            ones_max = 0
            for c in block:
                if c == '1':
                    ones += 1
                else:
                    if ones > ones_max:
                        ones_max = ones
                    ones = 0
            if M == 8:
                if ones_max <= 1:
                    v[0] += 1
                elif ones_max == 2:
                    v[1] += 1
                elif ones_max == 3:
                    v[2] += 1
                else:
                    v[3] += 1
            elif M == 128:
                if ones_max <= 4:
                    v[0] += 1
                elif ones_max == 5:
                    v[1] += 1
                elif ones_max == 6:
                    v[2] += 1
                elif ones_max == 7:
                    v[3] += 1
                elif ones_max == 8:
                    v[4] += 1
                else:
                    v[5] += 1
            elif M == 10000:
                if ones_max <= 10:
                    v[0] += 1
                elif ones_max == 11:
                    v[1] += 1
                elif ones_max == 12:
                    v[2] += 1
                elif ones_max == 13:
                    v[3] += 1
                elif ones_max == 14:
                    v[4] += 1
                elif ones_max == 15:
                    v[5] += 1
                else:
                    v[6] += 1
        chi_sq = 0.0
        for i in range(K + 1):
            chi_sq += pow((v[i] - N * self.data[ind_data][3][i]), 2) / (N * self.data[ind_data][3][i])
        p_val = gammaincc(K / 2.0, chi_sq / 2)
        return p_val >= 0.01


