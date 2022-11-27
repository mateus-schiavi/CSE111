import matplotlib.pyplot as plt 
import numpy as np
import pytest

def test_number():
    data = np.arange(8) + 1j*np.arange(2, 10) 
    x = data.real 
    y = data.imag
    
def test_plot():
    plt.plot(x, y, '-.r*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show()

pytest.main(["-v", "--tb=line", "-rN", __file__])