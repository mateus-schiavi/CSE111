from sympy import Symbol, solve, init_printing
from sympy.plotting import plot

# configuração para outputs melhores no artigo, pode ser ignorado
init_printing(use_latex='png', scale=1.25, order='grlex',
              forecolor='Black', backcolor='White', fontsize=12)

x = Symbol('x')
example = (x + 1)**2 + 9

plot(example, axis_center=(0, 0))