import matplotlib.pyplot as plt 
import numpy as np
import cmath
 
print("WELCOME TO COMPLEX NUMBERS CALCULATOR")
print("|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|")

def perform_operation(x, y, x1, y1, z):
    if z.lower() == "sum":
        result = complex((x + 1j*y) + (x1 + 1j*y1))
        return f"{x} + {y}j + {x1} + {y1}j = {result.real} + {result.imag}j"
    elif z.lower() == "minus":
        result = complex((x + 1j*y) - (x1 + 1j*y1))
        return f"{x} + {y}j - {x1} + {y1}j = {result.real} + {result.imag}j"
    elif z.lower() == "times":
        result = complex((x + 1j*y) * (x1 + 1j*y1))
        return f"({x} + {y}j) * ({x1} + {y1}j) = {result.real} + {result.imag}j"
    elif z.lower() == "division":
        result = complex((x + 1j*y) / (x1 + 1j*y1))
        return f"({x} + {y}j) / ({x1} + {y1}j) = {result.real} + {result.imag}j"
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

        
if __name__  == "__main__":
    main()
