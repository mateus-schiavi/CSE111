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
    
def test_function():
    # make data
    X = np.arange(0, math.pi*2, 0.05) 
    Y1 = np.sin(X) 
    Y2 = np.cos(X) 
    Y3 = np.tan(X) 
    Y4 = np.tanh(X) 
    figure, axis = plt.subplots(2, 2) 
    axis[0, 0].plot(X, Y1) 
    axis[0, 0].set_title("Sine Function") 
    axis[0, 1].plot(X, Y2) 
    axis[0, 1].set_title("Cosine Function") 
    axis[1, 0].plot(X, Y3) 
    axis[1, 0].set_title("Tangent Function") 
    axis[1, 1].plot(X, Y4) 
    axis[1, 1].set_title("Tanh Function") 
    plt.show()


pytest.main(["-v", "--tb=line", "-rN", __file__])