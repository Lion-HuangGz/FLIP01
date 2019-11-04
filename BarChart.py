import numpy as np
import matplotlib.pyplot as plt

N=5

y1=[20,10,30,25,15]
y2=[22,5,40,20,15]

x=np.arange(N)
"""
pl=plt.bar(x,y1,color='red',width=0.5)
plt.show()
"""

"""
pl=plt.barh(x,y1)
plt.show()
"""

"""
bar_width=0.3
pl=plt.bar(x,y1,bar_width,color='r')
pl=plt.bar(x+bar_width,y2,bar_width,color='b')
plt.show()
"""

pl=plt.bar(x,y1,color='r')
pl=plt.bar(x,y2,color='b',bottom=y1)
plt.show()