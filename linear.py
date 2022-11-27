import matplotlib.pyplot as plt 
import numpy as np 
data = np.arange(8) + 1j*np.arange(-4, 4) 
x = data.real 
y = data.imag 
plt.plot(x, y, '-.r*') 
plt.ylabel('Imaginary') 
plt.xlabel('Real') 
plt.show()

pytest.main(["-v", "--tb=line", "-rN", __file__])