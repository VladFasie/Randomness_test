from monobit_test import MonoBit
from maurer_test import Maurer
from longestRunOfOnes_test import LongestRunOfOnes
from frequencyBlock_test import FrequencyBlock
from binaryMatrix_test import BinaryMatrix
from serial_test import Serial
from runs_test import Runs
from os import listdir, path

current_dir = path.dirname(path.realpath(__file__))
data_dir = path.join(current_dir, 'data')
for filename in listdir(data_dir):
    f = open(path.join(data_dir, filename), 'r')
    data = [int(item) for item in f.readlines()]

    print('___________________________________')
    print('########\t', filename, '\t########')
    print('___________________________________')

    passed = 0

    mb = MonoBit()
    result = mb.test(data)
    if result:
        passed += 1
    print('monobit: ', 'passed' if result else 'failed')

    ma = Maurer(8, 2560)
    result = ma.test(data)
    if result:
        passed += 1
    print('maurer: ', 'passed' if result else 'failed')

    lro = LongestRunOfOnes()
    result = lro.test(data)
    if result:
        passed += 1
    print('longest run of ones: ', 'passed' if result else 'failed')

    bm = BinaryMatrix()
    result = bm.test(data)
    if result:
        passed += 1
    print('binary matrix: ', 'passed' if result else 'failed')

    fb = FrequencyBlock(22000)
    result = fb.test(data)
    if result:
        passed += 1
    print('frequency block: ', 'passed' if result else 'failed')

    r = Runs()
    result = r.test(data)
    if result:
        passed += 1
    print('runs: ', 'passed' if result else 'failed')

    s = Serial()
    result = s.test(data)
    if result:
        passed += 1
    print('serial: ', 'passed' if result else 'failed')

    print('___________________________________')
    print('#######\tpassed ', passed, ' / 7\t#######')
    print('___________________________________')

    f.close()