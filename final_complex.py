import matplotlib.pyplot as plt 
import numpy as np
import pytest
import cmath

x = int(input("Enter the real number of the equation: "))
y = int(input("Enter the real number of the equation: "))
print(complex(x + 1j*y))

plt.plot(x,y,'k--')
plt.show()