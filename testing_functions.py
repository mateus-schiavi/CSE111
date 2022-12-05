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

def test_seno():
    X = np.arange(0, math.pi*2, 0.05) 
    y = np.sin(X) 
    z = np.cos(X) 
    plt.plot(X, y, color='r', label='sin') 
    plt.plot(X, z, color='g', label='cos') 
    plt.xlabel("Angle") 
    plt.ylabel("Magnitude") 
    plt.title("Sine and Cosine functions") 
    plt.legend() 
    plt.show()
    
pytest.main(["-v", "--tb=line", "-rN", __file__])