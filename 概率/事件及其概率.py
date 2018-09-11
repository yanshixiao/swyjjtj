# -*- coding: utf-8 -*-
# __author__ = 'Administrator'
import itertools
from fractions import Fraction
import numpy as np


def q_14():
    print(1/4)
    print(2/4)
    print(3/4)


def q_16():
    print(6*6)
    # product笛卡尔积，有放回的排列，多步骤试验计数，如两个骰子也可归为此类
    print(list(itertools.product([1, 2, 3, 4, 5, 6], repeat=2)))
    print(6/36)
    lst = list(itertools.product([1, 2, 3, 4, 5, 6], repeat=2))
    sum1 = 0
    for i in lst:
        if i[0]+i[1] >= 9:
            sum1 += 1
    print(Fraction(sum1, 36))
    sum2 = 0
    for i in lst:
        if sum(list(i)) % 2 == 0:
            sum2 += 1
    print("不同意", Fraction(sum2, 36))
    print("古典法")


def q_18():
    array = np.array([53, 32, 21, 50, 28, 23, 52, 24])
    print(Fraction(53,500))
    print(Fraction(53+50+52, 500))
    print(Fraction(sum(array), 500))


def q_20():
    array = np.array([191, 467, 244, 42])
    print(191/944, 467/944, 244/944, 42/944)
    print((191+467)/944)
    print((244+42)/944)


def main():
    # q_14()
    # q_16()
    # q_18()
    q_20()
    pass


if __name__ == "__main__":
    main()