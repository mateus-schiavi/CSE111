import matplotlib.pyplot as plt 
import numpy as np
import cmath
import pytest

x= int(input("Please enter the real number of the equation: "))
y = int(input("Please enter the imaginary number of the equation: "))
print(complex(x + 1j*y))


plt.plot(x,y, '-.r*')
plt.xlabel('Real')
plt.ylabel('Imaginary') 
plt.show()
plt.figure()
