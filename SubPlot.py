import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,100)
"""
面向对象的方式
fig=plt.figure()  #图像

ax1=fig.add_subplot(221) #2*2的子图结构

ax1.plot(x,x)

ax2=fig.add_subplot(222)

ax2.plot(x,x)

ax3=fig.add_subplot(223)

ax3.plot(x,x)

ax4=fig.add_subplot(224)

ax4.plot(x,x)
"""

plt.subplot(221)
#plt.subplot(222)
#plt.subplot(223)
#plt.subplot(224)
plt.plot(x,-x*x)
plt.show()