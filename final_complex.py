import matplotlib.pyplot as plt 
import numpy as np
import cmath
import pytest

print("WELCOME TO COMPLEX NUMBERS CALCULATOR")
print("|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|")

def perform_operation(x, y, x1, y1, z):
    sum = 0
    minus = 0
    times = 0
    division = 0
    if z.lower() == "sum":
        return complex((x + 1j*y) + (x1 + 1j*y1))
    elif z.lower() == "minus":
        return complex((x + 1j*y) - (x1 + 1j*y1))
    elif z.lower() == "times":
        return complex((x + 1j*y) * (x1 + 1j*y1))
    elif z.lower() == "division":
        return complex((x + 1j*y) / (x1 + 1j*y1))
    else:
        return None

def main():
    x = int(input("Enter the real part of the equation: "))
    y = int(input("Enter the imaginary part of the equation: "))
    x1 = int(input("Enter the second real part of the equation: "))
    y1 = int(input("Enter the second imaginary part of the equation: "))
    z = (input("What kind of operation you want to compute (+,-,*,/)? "))
    result = perform_operation(x, y, x1, y1, z)
    if result:
        print(result)
    else:
        print("Try Again, please.")
        
    repeat()
    
    
def repeat():
    answer = input("Would you like to compute again? ")
    if answer.lower() == "yes":
        main()
    elif answer.lower() == "no":
        print("The program will now end!")
    else:
        print("Invalid answer.")
        repeat()

def test_perform_operation():
    assert perform_operation(1, 2, 3, 4, "sum") == (4 + 6j)
    assert perform_operation(1, 2, 3, 4, "minus") == (-2 - 2j)
    assert perform_operation(1, 2, 3, 4, "times") == (-5 + 10j)
    assert perform_operation(1, 2, 3, 4, "division") == (0.44 + 0.08j)
    assert perform_operation(1, 2, 3, 4, "invalid") == None
        
if __name__  == "__main__":
    main()
