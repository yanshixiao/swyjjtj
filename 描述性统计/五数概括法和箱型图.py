# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import numpy as np
import matplotlib.pyplot as plt


def q_46():
    array = np.array([27, 50, 20, 15, 30, 34, 28, 25])
    print("最小值", np.min(array))
    print("第一四分位数", np.percentile(array, 25))
    print("中位数", np.median(array))
    print("第三四分位数", np.percentile(array, 75))
    print("最大值", np.max(array))


def q_48():
    array = np.array([5, 15, 18, 10, 8, 12, 16, 10, 6])
    print("最小值", np.min(array))
    print("第一四分位数", np.percentile(array, 25))
    print("中位数", np.median(array))
    print("第三四分位数", np.percentile(array, 75))
    print("最大值", np.max(array))
    import matplotlib.pyplot as plt

    # sym 调整好异常值的点的形状
    # whis 默认是1.5， 通过调整它的数值来设置异常值显示的数量，
    # 如果想显示尽可能多的异常值，whis设置很小，否则很大
    plt.boxplot(array, sym="o", whis=1.5)
    # plt.boxplot(data, sym ="o", whis = 0.01)
    # plt.boxplot(data, sym ="o", whis = 999)
    plt.show()


def q_50():
    array_man = np.array([65.30, 66.27, 66.52, 66.85, 70.87, 87.18, 96.54])
    array_women = np.array([90.32, 92.18, 98.70, 106.55, 107.26])
    array_all = np.append(array_man, array_women)
    array_all.sort()
    print("第", np.argwhere(array_all == 90.32)+1, "名")
    print("男", np.median(array_man))
    print("女", np.median(array_women))
    print("最小值", np.min(array_man), "第一四分位数", np.percentile(array_man, 25), "中位数", np.percentile(array_man, 75),
          "第三四分位数", np.percentile(array_man, 75), "最大值", np.max(array_man))
    mq25, mq75 = np.percentile(array_man, [25, 75])
    iqr_m = mq75 - mq25
    min_m = mq25 - 1.5 * iqr_m
    max_m = mq75 + 1.5 * iqr_m
    for x in array_man:
        if x > max_m or x < min_m:
            print("有异常值")

    plt.boxplot(array_man)
    plt.show()
    plt.boxplot(array_women)
    plt.show()


def q_52():
    array_T_Mobile = np.array([71, 74, 70, 74, 73, 77, 75, 74, 68, 73, 75, 71, 76, 75, 72, 73, 74, 74, 73, 71])
    med = np.median(array_T_Mobile)
    q25, q75 = np.percentile(array_T_Mobile, [25, 75])
    iqr = q75 - q25
    min = np.min(array_T_Mobile)
    max = np.max(array_T_Mobile)
    print(min, q25, med, q75, max)
    maxv = q75 + 1.5 * iqr
    minv = q25 - 1.5 * iqr
    for x in array_T_Mobile:
        if x > maxv or x < minv:
            print("有异常值")
    plt.boxplot(array_T_Mobile)
    plt.show()


def main():
    # q_46()
    # q_48()
    # q_50()
    q_52()


if __name__ == "__main__":
    main()