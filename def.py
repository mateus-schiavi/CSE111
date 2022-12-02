import matplotlib.pyplot as plt 
import numpy as np
import cmath
import pytest

def get_number():
    a = int(input("Please enter the real number: "))
    b = int(input("Please enter the imaginary number: "))
    c = complex(a + b)
    
pytest.main(["-v", "--tb=line", "-rN", __file__])