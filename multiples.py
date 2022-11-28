import matplotlib.pyplot as plt 
import numpy as np 
import math
import pytest

def test_function():
    plt.figure(1) # a primeira janela
    plt.subplot(2,1,1) # o primeiro gráfico na primeira janela
    plt.plot((1,2,3))
    plt.subplot(2,1,2) # o segundo gráfico na primeira janela
    plt.plot((4,5,6))

    plt.figure(2) # uma segunda janelaplt.plot((4,5,6)) # cria o gráfico em subplot(1,1,1) por padrão
    plt.figure(1) # torna a janela 1 a janela corrente; subplot(2,1,2) ainda é o gráfico corrente
    plt.subplot(2,1,1) # faz subplot(2,1,1) na janela 1 o gráfico corrente
    plt.title(u'fácil como 1,2,3') # Título do gráfico 2,1,1
    plt.show()

pytest.main(["-v", "--tb=line", "-rN", __file__])