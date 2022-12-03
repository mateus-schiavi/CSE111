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
    
    z = complex(x+1j*y)
    print("The respective formula is {z}")   
    repeat()
    
def repeat():
    answer = input("Would you like to compute again? ")
    if answer.lower() == "yes":
        main()
    elif answe.lower() == "no":
        print("The program will now end!")
    else:
        print("Invalid answer.")
        repeat()
        
while running:
    result = input("Do you love complex numbers? ")
    if result.lower() == "yes":
        print("If you love complex numbers, you can be the next Stephen Hawking.")
        loop = True;
    elif result.lower() == "no":
        print("I understand. You're far from being a genious.")
        result = ("")
        loop = False;
    else:
        print("Please enter yes or no")
        
main()