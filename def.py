import matplotlib.pyplot as plt 
import numpy as np
import cmath
import pytest

x= int(input("Please enter the real number of the equation: "))
y = int(input("Please enter the imaginary number of the equation: "))
print(complex(x + 1j*y))

fig, ax = plt.subplots()
ax.plot(x, y, linewidth=2.0)
plt.plot(x,y, '-.r*')
plt.ylabel('Imaginary') 
plt.xlabel('Real')
plt.show()
