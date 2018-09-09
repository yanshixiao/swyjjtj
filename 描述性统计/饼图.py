import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

labels=['China','Swiss','USA','UK','Laos','Spain']
x = [222, 42, 455, 664, 454, 334]
explode = [0, 0.1, 0, 0, 0, 0] # 0.1 凸出这部分，

fig = plt.figure()
plt.pie(x, labels=labels, explode=explode, autopct='%1.2f%%')
plt.title("Pie chart")

plt.show()
plt.savefig("PieChart.jpg")