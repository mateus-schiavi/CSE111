import matplotlib.pyplot as plt

def cubo(w):                            
    return w*w*w   

x = np.linspace(0, 3, 20)
y = cubo(x)

plt.plot(x, y)       # gráfico de linha
plt.plot(x, y, 'o')  # gráfico com pontos
plt.show()           # mostra o gráfico