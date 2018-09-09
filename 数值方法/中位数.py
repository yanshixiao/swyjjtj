import numpy as np

def mid(lst):
    """
    计算中位数
    :param lst:
    :return:
    """
    lst.sort()
    print(lst)

    while len(lst)>2:
        lst = lst[1: -1]
    if len(lst) == 1:
        return lst[0]
    else:
        return np.mean(tuple([lst[0], lst[1]]))

a = [1, 3, 2, 6, 4, 5]
r = mid(a)
print(r)