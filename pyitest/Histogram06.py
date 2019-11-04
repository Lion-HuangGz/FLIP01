import numpy as np
import matplotlib.pyplot as plt

"""

mu=100 #均值为100 mean of distribution
sigma=20 #标准差为20 standard devitation of distribution

x=mu+sigma*np.random.randn(2000)
"""np.random.randn(d0,d1,d2……dn)
1)当函数括号内没有参数时，则返回一个浮点数；
2）当函数括号内有一个参数时，则返回秩为1的数组，不能表示向量和矩阵；
3）当函数括号内有两个及以上参数时，则返回对应维度的数组，能表示向量或矩阵；
4）np.random.standard_normal（）函数与np.random.randn()类似，但是np.random.standard_normal（）的输入参数为元组（tuple）.
5)np.random.randn()的输入通常为整数，但是如果为浮点数，则会自动直接截断转换为整数。
"""

 #plt.hist(x,bins=10,color='red',normed=True) #normed 标准化
plt.hist(x,bins=50,color='green',normed=False)
plt.show()

"""



x=np.random.randn(1000)+2
y=np.random.randn(1000)+3

plt.hist2d(x,y,bins=40)
plt.show()