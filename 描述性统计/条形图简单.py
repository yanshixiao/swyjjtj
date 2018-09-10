import numpy as np
import matplotlib as mpl
import numpy.random as random
import matplotlib.pyplot as plt

mpl.rcParams['axes.titlesize'] = 20
mpl.rcParams['xtick.labelsize'] = 16
mpl.rcParams['ytick.labelsize'] = 16
mpl.rcParams['axes.labelsize'] = 16
mpl.rcParams['xtick.major.size'] = 0
mpl.rcParams['ytick.major.size'] = 0

tvs = ['WoF', 'Jep', 'JJ', 'THM', 'OWS']

a = np.array(tvs)
b = random.choice(a, 50)
wof_count = b.tolist().count('WoF')
jep_count = b.tolist().count('Jep')
jj_count = b.tolist().count('JJ')
thm_count = b.tolist().count('THM')
ows_count = b.tolist().count('OWS')

fig = plt.figure('Bar chart & Pie chart')

ax = fig.add_subplot(1,2,1)
ax.set_title('Company Name')

xticks = np.arange(5)
# 柱状图每个柱的宽度
bar_width = 0.5
# 节目名称
tv_name = tvs
# 出现次数
nums = [wof_count, jep_count, jj_count, thm_count, ows_count]

bars = ax.bar(xticks, nums, width=bar_width, edgecolor='none')

ax.set_ylabel('出现次数')
# x轴每个标签的具体位置，设置为每个柱的中央
ax.set_xticks(xticks+bar_width/2)
# 设置每个标签的名字
ax.set_xticklabels(tv_name)

# 设置x轴的范围
ax.set_xlim([bar_width/2 - 0.5, 5 - bar_width / 2])

# 设置y轴的范围
ax.set_ylim([0, 20])

plt.show()
