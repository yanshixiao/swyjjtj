import itertools

# 笛卡尔积（有放回抽样）AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
for i in itertools.product('ABCD', repeat=2):
    print(''.join(i), end=' ')
print()

# 排列
for i in itertools.permutations('ABCD', 2):
    print(i, end=' ')
print("============================")

# 组合
for i in itertools.combinations('ABCD', 2):
    print(i, end=' ')
print("============================")