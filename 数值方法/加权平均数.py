import numpy as np

a = (70, 80, 60)

np.mean(a)  # 平均值

r = np.average(a, weights=[3, 3, 4])  # 加权平均值

print(r)
