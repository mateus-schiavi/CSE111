import matplotlib.pyplot as plt 
import numpy as np
import pytest

def test_number():
    data = np.arange(4) + 1j*np.arange(2,6)
    x = data.real 
    y = data.imag
    plt.plot(x, y, '-.r*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 

    
def test_function():
    # make data
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)

    # plot
    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)

    ax.set(xlim=(x, y), xticks=np.arange(x, y),
        ylim=(x, y), yticks=np.arange(x, y))


pytest.main(["-v", "--tb=line", "-rN", __file__])