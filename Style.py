import numpy as np
import matplotlib.pyplot as plt

y=np.arange(5)


plt.plot(y)
"""
plt.plot(y+1,color='r',marker='>','--')  #虚线
plt.plot(y+2,color='0.9',marker='<','-.')  # 颜色深浅，点划线
plt.plot(y+3,color='#FF00FF',marker='o',':')  # 16进制，颜色代码可以直接百度查询，点线
plt.plot(y+4,color='0.1,0.2,0.3',marker='D','-')  #RGB元组，实线
 #没有加颜色，但是做出的图形依然有颜色，这是系统默认的颜色排序
 #线形只有四种：实线、虚线、 点划线、点线
"""

plt.plot(y,'cx--') #将颜色、点型、线性放入同一个字符串中进行表示
plt.show()