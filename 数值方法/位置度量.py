# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import numpy as np
from scipy import stats


def q_2():
    # 2.平均数中位数
    array = np.array([10, 20, 21, 17, 16])
    average_num = np.mean(array)
    print(average_num)
    median_num = np.median(array)
    print(median_num)


def q_4():
    # 4.平均增长率
    average_up = pow((1 - 0.06) * (1 - 0.08) * (1 - 0.04) * (1 - 0.02) * (1 - 0.54), 1 / 10)
    average_up_rate = (average_up - 1) * 100
    print(average_up_rate)
    print("======================================================")


def q_6():
    # 6.三个值
    array2 = np.array([53, 55, 70, 58, 64, 57, 53, 69, 57, 68, 53])
    avg_num = np.mean(array2)
    med_num = np.median(array2)
    counts = np.bincount(array2)
    mode_num = np.argmax(counts)
    mode_num2 = stats.mode(array2)
    print(avg_num)
    print(med_num)
    print(np.argmax(counts))
    print(mode_num2)
    print("======================================================")


def q_8():
    # 8.华尔街
    array3 = np.array([108, 83, 106, 73, 53, 85, 80, 63, 67, 75, 124, 55, 93, 118, 77])
    median = np.median(array3)
    print(median)
    mean = np.mean(array3)
    print(mean)
    # 一三四分位数
    first_four_num = np.percentile(array3, 25)
    second_four_num = np.percentile(array3, 50)
    third_four_num = np.percentile(array3, 75)
    print(first_four_num)
    print(second_four_num)
    print(third_four_num)
    print("======================================================")


def q_10():
    array10 = np.array([42,66,67,71,78,62,76,71,67,61,64,61,54,83,63,68,69,81,53])
    print(np.mean(array10))
    print(np.median(array10))
    print(stats.mode(array10))
    print(np.percentile(array10, 25))
    print(np.percentile(array10, 50))
    print(np.percentile(array10, 75))
    print(np.percentile(array10, 90))


def q_12():
    array11 = np.array([14.1,14.7,14.6,13.6,13.6,14.9,14.5,16.0,15.9,15.1,14.0,16.1,15.8,16.1,16.5,16.2,15.7,16.2,15.0,14.0,13.1])
    print(np.max(array11))
    print(np.min(array11))
    print(np.mean(array11))
    print(np.median(array11))
    print(stats.mode(array11))
    print(np.percentile(array11,25))
    print(np.percentile(array11,50))
    print(np.percentile(array11,75))


def q_14():
    pass


def main():
    # q_10()
    # q_12()
    q_14()


if __name__ == "__main__":
    main()
