import numpy as np
import matplotlib.pyplot as plt

np.random.seed(200)
#data=np.random.normal(size=1000,loc=0,scale=1)
#plt.boxplot(data,sym='o',whis=0.05)


data=np.random.normal(size=(1000,4),loc=0,scale=1)
#size=(1000,4)  4*1000的数组
labels=['A','B','C','D']
plt.boxplot(data,labels=labels)
plt.show()



