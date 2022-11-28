import matplotlib.pyplot as plt 
import numpy as np
import pytest

def figure_1():
    data = np.arange(2) + 1j*np.arange(1,3)
    x = data.real 
    y = data.imag
    plt.plot(x, y, '-.r*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show()
pytest.main(["-v", "--tb=line", "-rN", __file__])