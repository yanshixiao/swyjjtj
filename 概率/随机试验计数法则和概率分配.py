# -*- coding: utf-8 -*-
# __author__ = 'Administrator'
import itertools


def q_2():
    result = list(itertools.combinations(['A','B','C','D','E','F'], 3))
    print(len(result))
    print(result)


def q_4():
    pass


def q_6():
    print(20/50)
    print(13/50)
    print(17/50)


def q_8():
    pass


def q_10():
    print(86.5/100)
    print("小于2的除以总数10", 3/10)
    print("大于1的除以总数10", 5/10)
    print((1-87.1)/100)


def q_12():
    list1 = list(itertools.combinations([x for x in range(1, 60)], 5))
    rlt1 = len(list1)
    list2 = list(itertools.combinations([x for x in range(1,36)], 1))
    rlt2 = len(list2)
    print(rlt1*rlt2)
    print(1/(rlt1*rlt2))


def main():
    # q_2()
    # q_6()
    # q_10()
    q_12()


if __name__ == "__main__":
    main()