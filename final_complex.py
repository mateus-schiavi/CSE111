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

#Time—50%: Did you spend at least three hours on your Python program or test functions during the current lesson? Yes
#Is your program organized into multiple functions? Yes
#Does each function in your program perform just one task? Yes, after showing the complex equation, the program asks if the user wants to compute again.
#Did you complete some significant part of your program during the current week? Yes, the code above is the first part of my project.
#A list of the function names in your program: I used the main function and the refeat function, both with def. 
#A list of the test function names in your test code: I've used the function below:
#def test_number():
#    data = np.arange(8) + 1j*np.arange(2, 10)
#   x = data.real 
#    y = data.imag
#   plt.plot(x, y, '-.r*') 
#    plt.ylabel('Imaginary') 
#    plt.xlabel('Real') 
#    plt.show()  
#pytest.main(["-v", "--tb=line", "-rN", __file__])

#A list of the documentation that you read, the videos that you watched, and the coding experiments that you tried.
#https://www.geeksforgeeks.org/complex-numbers-in-python-set-1-introduction/#:~:text=An%20complex%20number%20is%20represented,be%20represented%20by%20imag().
#https://realpython.com/python-complex-numbers/
#https://www.tutorialspoint.com/complex-numbers-in-python
#https://matplotlib.org/stable/plot_types/index.html
# A description or list of the work that you finished on your program : my program is based on operations with complex numbers.
# A complex number is followed by a letter, more specifically, the letter j, for example, in the equation: 2 + 3j: 2 is the real number, while
# 3 is the imaginary number, this happens because j = sqrt(-1).

#In the second part, I'll try to put two complex equations in the same plot.