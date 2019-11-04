import numpy as np
import matplotlib.pyplot as plt

x=np.arange(1,11,1)

"""matplotlib方式：


"""
plt.plot(x,x*2,label='Normal')
plt.plot(x,x*3,label='Fast')
plt.plot(x,x*4,label='Faster')
plt.plot(x,x*5,label='F1')
plt.legend(ncol=2,loc=4)
"""
#或者直接再legend函数里面写标签：

plt.plot(x,x*2)
plt.plot(x,x*3)
plt.plot(x,x*4)
plt.plot(x,x*5)
plt.legend(['F1','F2','F3','F4'],loc='best',ncol=2)
plt.show()
"""


#面向对象方式：

fig=plt.figure()
ax=fig.add_subplot(111)
l,=plt.plot(x,x)  #L,是什么意思
ax.legend(['1'])
plt.show()