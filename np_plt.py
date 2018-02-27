"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
x = np.array([[1,2,3], [4,5,6]], np.int32)
print type(x)
print x.shape
print x.dtype

z = np.arange(3, dtype = np.uint8)
print z
print z.dtype

a = np.arange(5)



import matplotlib.pyplot as plt

xs = [1,2,3,4,5,6]
ys = [1,4,9,16,25,36]

plt.plot(xs, ys)



import matplotlib.pyplot as plt

xs = [1,2,3,4,5,6]
ys = [x**2 for x in xs]

plt.plot(xs,ys)
plt.xlabel("x-axis")
plt.xlabel("y-axis")
plt.title("Matplotlib Example")
plt.savefig(quad.png)
plt.show()

