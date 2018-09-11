# -*- coding: utf-8 -*-
# __author__ = 'Administrator'

from fractions import Fraction


def q_22():
    ALL = ["E1", "E2", "E3", "E4", "E5"]
    A = ["E1", "E2"]
    B = ["E3", "E4"]
    C = ["E2", "E3", "E5"]
    print(Fraction(2, 5))
    print(Fraction(2, 5))
    print(Fraction(3, 5))
    print("A U B", Fraction(2+2, 5), "互斥")
    print("A补集: {E3,E4,E5}", "C补集：{E1,E4}", "P(A补集)", (5-2)/5, "P(C补集)", (5-3)/5)
    b_difference = set(ALL).difference(set(B))
    a_bdiff_union = set(A).union(b_difference)
    print(a_bdiff_union, len(a_bdiff_union)/5)
    print(len(set(B).union(set(C)))/5)


def q_24():
    print(1-(0.04+0.26+0.65))  # 结果数字有误差
    print((0.05+0.65))
    # TODO: 探求原因


def q_26():
    PA = 16/25
    print(PA)
    PB = (25-13)/25
    print(PB)
    PA_intersection_B = (7+2)/25
    print(PA_intersection_B)
    PA_union_B = PA + PB - PA_intersection_B
    print(PA_union_B)



def main():
    # q_22()
    # q_24()
    q_26()
    pass


if __name__ == "__main__":
    main()