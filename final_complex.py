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
    print(z)
    
    repeat()
    
def repeat():
    answer = input("Would you like to compute again? ")
    if answer.lower() == "y":
        main()
    if answe.lower() == "n":
        print("The program will now end!")
    else:
        print("Invalid answer. Please answer with y/n")
        repeat()
        
while running:
    result = input("Do you love complex numbers? ")
    if result.lower() == "y":
        print("If you love complex numbers, you can be the next Stephen Hawking.")
        loop = True;
    if result.lower() == "n":
        print("I understand. You're far from being a genious.")
        loop = False;
    else:
        print("Wrong Answer. Please answer with y/n")