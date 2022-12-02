import matplotlib.pyplot as plt 
import numpy as np
import cmath
import pytest

a = int(input("Please enter the real number: "))
b = int(input("Please enter the imaginary number: "))
print(complex(a + 1j*b))

data = np.arange(2) + 1j*np.arange(3,5)
x = data.real 
y = data.imag
plt.plot(x, y, '-.r*') 
plt.ylabel('Imaginary') 
plt.xlabel('Real') 
