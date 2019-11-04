import matplotlib.pyplot as plt
import numpy as np


x=np.arange(-10,11,1)

plt.plot(x,x*x)

#plt.axis([-2,2,0,10])
#print(plt.axis())

#plt.ylim([0,10])
#plt.xlim([-5,5])  #只调x轴

plt.xlim(xmin=-10,xmax=100)

plt.show()