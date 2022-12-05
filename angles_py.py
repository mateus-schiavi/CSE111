import sympy

from sympy import (sin, cos, tan, asin, acos, atan, sqrt, symbols, simplify,
                   trigsimp, log, exp, expand, expand_trig, Symbol, rad, deg,
                   sinh, cosh, tanh)

from sympy.plotting import (plot, plot3d, plot3d_parametric_line,
                            plot_implicit, plot3d_parametric_surface)

import numpy as np

import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter, MultipleLocator

# configuração para outputs melhores no artigo, pode ser ignorado
sympy.init_printing(use_latex='png', scale=1.0, order='grlex',
                    forecolor='Black', backcolor='White',)