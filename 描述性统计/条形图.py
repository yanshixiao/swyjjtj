from matplotlib import pyplot as plt
import numpy as np

# 中文乱码的处理
plt.rcParams['font.sans-serif'] =['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False

#第一步，取出一张白纸
fig = plt.figure(1)

#第二步，确定绘图范围，由于只需要画一张图，所以我们将整张白纸作为绘图的范围(111等同于1,1,1 表示一行一列的第一个)
ax1 = plt.subplot(111)

#第三步，整理我们准备绘制的数据
data = np.array([15, 20, 18, 25])

#第四步，准备绘制条形图，思考绘制条形图需要确定那些要素
#1、绘制的条形宽度
#2、绘制的条形位置(中心)
#3、条形图的高度（数据值）
width=0.5
x_bar = np.arange(4)

#第五步，绘制条形图的主体，条形图实质上就是一系列的矩形元素，我们通过plt.bar函数来绘制条形图
rect = ax1.bar(left=x_bar, height=data, width=width, color="lightblue")

#第六步，向各条形上添加数据标签
for rec in rect:
    x=rec.get_x()
    height=rec.get_height()
    ax1.text(x+0.1,1.02*height,str(height))

#第七步，绘制x，y坐标轴刻度及标签，标题
ax1.set_xticks(x_bar)
ax1.set_xticklabels(("first", "second", "third", "fourth"))
ax1.set_ylabel("sales")
ax1.set_title("The Sales in 2016")
ax1.grid(True)
ax1.set_ylim(0, 28)
plt.show()
