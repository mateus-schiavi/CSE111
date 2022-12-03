import matplotlib.pyplot as plt 
import numpy as np
import pytest
import cmath

running = True;

print("WELCOME TO COMPLEX NUMBERS CALCULATOR")
print("|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|")

def main():
    x = int(input("Enter the real part of the equation: "))
    y = int(input("Enter the imaginary part of the equation: "))
    plt.plot(x,y,'-.r*')
    plt.xlabel('Real')
    plt.ylabel('Imaginary')
    plt.show()
    
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
main()