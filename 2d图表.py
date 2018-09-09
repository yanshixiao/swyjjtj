import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

# 通过rcParams设置全局横纵轴字体大小
mpl.rcParams['xtick.labelsize'] = 24
mpl.rcParams['ytick.labelsize'] = 24

# 设置随机数种子
np.random.seed(42)

# x轴
x = np.linspace(0, 5, 100) # linspace 等差数列

# y轴
y = 2*np.sin(x) + 0.3*x**2
y_data = y + np.random.normal(scale=0.3, size=100)

# figure()指定图表名称
plt.figure('图表1')
# '.'标明画散点图，每个散点的形状是个圆
plt.plot(x, y_data, '.')

plt.figure('图表2')
plt.plot(x, y)

plt.figure('data & model')

# 通过'k'指定线的颜色，lw指定线的宽度
# 第三个参数除了颜色也可以指定线形，比如'r--'表示红色虚线
plt.plot(x, y, 'k', lw=3)

# scatter可以更容易地生成散点图
plt.scatter(x, y_data)

# 将当前figure的图保存到文件result.png
plt.savefig('result.png')

# 一定要加上这句才能让画好的图显示在屏幕上
plt.show()

