import math
import matplotlib.pyplot as plt


def f(x):
    return x**2+2*x+np.cos(x)

# intervalo de x
x = np.linspace(-3, 3, 50)

# definicao de y
y = f(x)

# plotando a funcao y=f(x)
a = plt.axes()
a.set_xlabel('x')
a.set_ylabel('y')
a.plot(x, y)