import numpy as np
import matplotlib.pyplot as plt

lables='A','B','C','D','E'
fracs=[15,20,35,10,25]
explode=[0,0.5,0,0,0]


plt.pie(x=fracs,labels=lables,autopct='%.0f%%',explode=explode,shadow=True)
#'%.0f%%' 格式化字符串,显示比例；
#explode表示该扇形离圆心的距离，突出显示
#shadow 表示扇形边的阴影
plt.show()