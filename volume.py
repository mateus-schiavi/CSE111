#Mateus Schiavi
#CSE 111
#01 Prove Milestone
import math
import pytest
from datetime import datetime

 
def main():
    print("Welcome to Tire Volume Calculator")
    print("|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|")

    while True:
        width = int(input("Enter the width of the tire in mm: "))
        aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
        diameter = int(input("Enter the diameter of the wheel in inches: "))

        volume = round(((math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000), 1)

        print(f"The respective volume is {volume} milliliters.")

        shopping = input("Would you like to buy tires with these dimensions? (yes/no) ")
        if shopping.lower() == "yes":
            phone_number = input("Please enter a phone number, and we will contact you at a later time: ")
            print("Have a great day!")
        elif shopping.lower() == "no":
            phone_number = ""
            print("Have a great day!")
        else:
            print("Error: Invalid Argument")
            continue

        current_date_and_time = datetime.now()

        with open("tire_volume.txt", "at") as tire_volume:
            print(f"\n{current_date_and_time}\n{width}, {aspect_ratio}, {diameter}, {volume}\n{phone_number}", file=tire_volume)

        answer = input("Would you like to compute another volume (Y/N)? ")
        if answer.upper() == "Y":
            continue
        elif answer.upper() == "N":
            print("The program will now end")
            break
        else:
            print("Error: Invalid Argument")
            break


if __name__ == '__main__':
    main()
    
    
# Pytest

def test_tire_volume():
    width = 205
    aspect_ratio = 55
    diameter = 16
    volume = round(((math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000), 1)
    assert volume == 472.6
