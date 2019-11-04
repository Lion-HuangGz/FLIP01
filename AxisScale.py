import matplotlib.pyplot as plt
import numpy as np
import datetime
import matplotlib as mpl
"""
x=np.arange(1,11,1)

plt.plot(x,x)

ax=plt.gca()

#ax.locator_params(nbins=5)
ax.locator_params('x',nbins=20)  #只调X轴，不动y轴
plt.show()
"""

#面向对象的方式，以横坐标为日期


fig=plt.figure()

start=datetime.datetime(2019,10,1) #起始日期
stop=datetime.datetime(2020,1,1)  #终止日期
delta=datetime.timedelta(days=1)  #日期间隔
dates=mpl.dates.drange(start,stop,delta)  #import matplotlib as mpl
y=np.random.rand(len(dates))
ax=plt.gca()
ax.plot_date(dates,y,linestyle='-',marker='')
date_format=mpl.dates.DateFormatter('%Y-%m-%d')
ax.xaxis.set_major_formatter(date_format)

fig.autofmt_xdate()  #自适应调增坐标位置
plt.show()