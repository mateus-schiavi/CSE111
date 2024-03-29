import matplotlib.pyplot as plt 
import numpy as np
import pytest

def test_number():
    data = np.arange(4) + 1j*np.arange(-2,2)
    x = data.real 
    y = data.imag
    plt.plot(x, y, '-.r*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show()

def test_two():
    data = np.arange(6) + 1j*np.arange(-3,3)
    x = data.real 
    y = data.imag 
    plt.plot(x, y, '-.r*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show()

def test_complex():
    data = np.arange(8) + 1j*np.arange(-4,4)
    x = data.real
    y = data.imag  
    plt.plot(x,y, '-.r*')
    plt.ylabel('Imaginary')
    plt.xlabel('Real')
    plt.show()
pytest.main(["-v", "--tb=line", "-rN", __file__])