# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import numpy as np


def q_24():
    array = np.array([10,20,12,17,16])
    # 方差
    variance = np.var(array)
    print(variance)
    # 标准差
    std = np.std(array)
    print(std)


def q_26():
    array = np.array([3.59, 3.59, 4.79, 3.56, 3.55, 3.71, 3.65, 3.60, 3.75, 3.56, 3.57, 3.59, 3.55, 3.99, 4.15, 3.66, 3.63, 3.73, 3.61, 3.57])
    # 平均价格
    print(np.mean(array))
    # 标准差
    print(np.std(array))


def q_28():
    array = np.array([191, 190, 187, 187, 187, 181, 181, 179, 179, 179, 179, 178, 178, 178, 178, 178, 178, 177, 177, 177])
    # 平均数
    print(np.mean(array))
    # 方差
    print(np.var(array))
    # 标准差
    print(np.std(array))


def q_30():
    array1 = np.array([11, 10, 9, 10, 11, 11, 10, 11, 10, 10])
    array2 = np.array([8, 10, 13, 7, 10, 11, 10, 7, 15, 12])
    # 极差
    print(array1.max()-array1.min())
    print(array2.max()-array2.min())
    # 标准差
    print(array1.std())
    # print(np.std(array1))
    print(array2.std())


def main():
    # q_24()
    # q_26()
    # q_28()
    q_30()


if __name__ == "__main__":
    main()