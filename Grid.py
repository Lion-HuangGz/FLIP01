import matplotlib.pyplot as plt
import numpy as np


"""
matplotlib方式绘制网格
y=np.arange(1,5)

plt.plot(y,y*2)
plt.grid(color='r',linewidth='2',linestyle='--')
plt.show()
"""








#面向对象方式绘制网格

x=np.arange(1,10,1) #生成一组数据
fig=plt.figure() #生成一张图
ax=fig.add_subplot(111) #生成坐标轴对象
plt.plot(x,x*2)
ax.grid(color='r')
plt.show()
