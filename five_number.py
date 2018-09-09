import random
import math
import time

def five_number(lst):
    max_number = max_(lst)
    min_number = min_(lst)
    avg_number = avg(lst)
    mid_number = mid(lst)
    mode_number = mode(lst)
    return (max_number, min_number, avg_number, mid_number, mode_number)


def max_(lst):
    if len(lst)<1:
        return None
    else:
        return max(lst)


def min_(lst):
    if len(lst)<1:
        return None
    else:
        return min(lst)

# 平均数
def avg(lst):
    if len(lst)<1:
        return None
    else:
        return float(sum(lst))/len(lst)


def mid(lst):
    if len(lst)<1:
        return None
    elif len(lst)%2==1:
        return lst[math.ceil(len(lst)/2.0)]
    else:
        return lst[int(len(lst)/2-1)]+lst[int(len(lst)/2)]/2.0


def mode(lst):
    # 统计list中各个数值出现的次数
    count_dict={}
    for i in lst:
        if i in count_dict.keys():
            count_dict[i]+=1
        else:
            count_dict[i]=1
    # 求出现次数的最大值
    max_appear=0
    for v in count_dict.values():
        if v > max_appear:
            max_appear = v
    if max_appear == 1:
        return
    mode_list = []
    for k, v in count_dict.items():
        if v == max_appear:
            mode_list.append(k)
    return mode_list


# arr = [1,2,3,2,3,1,4]
# print(five_number(arr))

arraylist=[i for i in range(1000000)]
random.shuffle(arraylist)
print(arraylist[2])
print(time.time(), "==============start")
result = five_number(arraylist)
print(result)
print(time.time(), "==============end")



