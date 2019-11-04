import matplotlib.pyplot as plt
import numpy as np

"""   #  pyplot方式
x=np.arange(2,20,1)
y1=x*x
y2=np.log(x)

plt.plot(x,y1)

plt.twinx()

plt.plot(x,y2,'r')
plt.show()
"""

#面向对象方式

x=np.arange(1,20,1)
y1=x*x
y2=np.log(x)
fig=plt.figure()
ax1=fig.add_subplot(111)#生成ax1对象
ax1.plot(x,y1)#生成图像
ax1.set_ylabel('Y1')
ax2=ax1.twinx()
ax2.plot(x,y2,'r')
ax2.set_ylabel('Y2')
ax1.set_xlabel('computer')
plt.show()