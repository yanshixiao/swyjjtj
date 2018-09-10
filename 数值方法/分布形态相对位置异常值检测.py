# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

import numpy as np


def q_36():
    array = np.array([520, 650, 500, 450, 280])
    for i in array:
        print((i-500)/100)


def q_38():
    pass


def q_40():
    print("1个标准差，68%")
    print("左边一个，右边两个标准差, ", 68/2-(95/2-68/2)+68/2, "%")
    print("超过两个标准差的部分，", 50-95/2, "%")


def q_42():
    print((2300-3100)/1200)
    print((4900-3200)/1200)
    print("z分数不大于3，也不小于3，都不算异常值")
    print("z分数", (13000-3200)/1200, "大于3，异常值")


def q_44():
    array_vin = np.array([90,85,75,78,71,65,72,76,77,76])
    array_lose = np.array([66,66,70,57,63,62,66,70,67,56])
    print("获胜队平均数：", np.mean(array_vin))
    print("获胜队标准差：", np.std(array_vin))
    print((84-np.mean(array_vin))/np.std(array_vin),"相差大约1个标准差,比例",(50-68/2))
    print((90-np.mean(array_vin))/np.std(array_vin),"相差大约2个标准差,比例",(50-95/2))
    print("-------")
    sub = np.subtract(array_vin, array_lose)
    print("得分差",sub)
    print("得分差平均数", np.mean(sub))
    print("得分差标准差", np.std(sub))

    q75, q25 = np.percentile(sub, [75, 25])
    iqr = q75 - q25
    min = q25 - 1.5 * iqr
    max = q75 + 1.5 * iqr
    print(min, max)
    for i in sub:
        if i < min or i > max:
            print("有异常值")


def main():
    # q_36()
    # q_40()
    # q_42()
    q_44()



if __name__ == "__main__":
    main()