import matplotlib.pyplot as plt 
import numpy as np
import pytest
import complex
 
def test_number():
    data = np.arange(8) + 1j*np.arange(2, 10)
    x = data.real 
    y = data.imag
    plt.plot(x, y, '-.r*') 
    plt.ylabel('Imaginary') 
    plt.xlabel('Real') 
    plt.show()
    
def test_real():
    # make data
    x = np.linspace(0, 10, 100)
    y = 4 + 2 * np.sin(2 * x)

    # plot
    fig, ax = plt.subplots()

    ax.plot(x, y, linewidth=2.0)

    ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
        ylim=(0, 8), yticks=np.arange(1, 8))

    plt.show()

pytest.main(["-v", "--tb=line", "-rN", __file__])