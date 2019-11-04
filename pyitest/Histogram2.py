import numpy as np
import matplotlib.pyplot as plt

x=np.random.randn(1000)+2  #以2为中心
y=np.random.randn(1000)+3  #以3为中心

plt.hist2d(x,y,bins=40)  #双变量的直方图，探索双变量的联合分布很好用
plt.show()