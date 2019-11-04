import numpy as np
import matplotlib.pyplot as plt
"""
height=[161,170,172,175,178,185]
weight=[60,65,70,75,78,80]
plt.scatter(height,weight)

"""
"""
N=1000
x=np.random.randn(N)
y=np.random.randn(N)
plt.scatter(x,y)
plt.show()
    """
""""
N=500
x=np.random.randn(N)
y=np.random.randn(N)*0.5
print(x,y)

plt.scatter(x,y)
plt.show()
"""

N=500
x=np.random.randn(N)
y=-x+np.random.randn(N)*0.5
print(x,y)

plt.scatter(x,y,s=30,c='black')
plt.show()