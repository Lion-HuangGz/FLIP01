import numpy as np
import matplotlib.pyplot as plt

"""
x=np.linspace(-10,10,5)
y=x**2
print(x,y)
plt.plot(x,y,)
plt.show()
"""

x=np.arange(0,1*np.pi,1)
y=np.sin(x)
plt.plot(x,y)
plt.show()