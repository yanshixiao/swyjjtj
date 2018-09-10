# -*- coding: utf-8 -*-
# __author__ = 'Administrator'
import numpy as np
import matplotlib.pyplot as plt


def q_56():
    x = [6, 11, 15, 21, 27]
    y = [6, 9, 6, 17, 12]
    plt.scatter(x, y)
    plt.show()
    covariance = np.cov(x, y)  # 得到的是一个协方差矩阵
    print(covariance[0][1])
    # 传统算法
    xmean = np.mean(x)
    ymean = np.mean(y)
    arrayx = np.array([i - xmean for i in x])
    arrayy = np.array([i - ymean for i in y])
    sum = np.sum(np.multiply(arrayx, arrayy))
    print(sum/4)
    # 相关系数
    print(np.corrcoef(x, y)[0][1])


def q_58():
    x = np.array([30, 50, 40, 55, 30, 25, 60, 25, 50, 55])
    y = np.array([28, 25, 25, 23, 30, 32, 21, 35, 26, 25])
    correlation =np.corrcoef(x, y)[0][1]
    print(correlation)


def main():
    # q_56()
    q_58()


if __name__ == "__main__":
    main()