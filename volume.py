#Mateus Schiavi
#CSE 111
#01 Prove Milestone
import math
from datetime import datetime

def main():
    width = int(input("Enter the width of the tire in mm: "))
    aspect_ratio = int(input("Enter the aspect ratio of the tire: "))
    diameter = int(input("Enter the diameter of the wheel in inches: "))

    volume = round(((math.pi * width ** 2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)) / 10000000), 1)

    print(f"The respective volume is {volume} milliliters.")
    return (width, aspect_ratio, diameter, volume)

def repeat():
    while True:
        answer = input("Would you like to compute another volume (Y/N)? ")
        if answer.upper() == "Y":
            main()
        elif answer.upper() == "N":
            print("The program will now end")
            return False
        else:
            print("Error: Invalid Argument")

def save_data(width, aspect_ratio, diameter, volume, phone_number):
    current_date_and_time = datetime.now()

    with open("tire_volume.txt", "at") as tire_volume:
        print(f"{current_date_and_time}\n{width}, {aspect_ratio}, {diameter}, {volume}\n{phone_number}\n", file=tire_volume)

def main_loop():
    while True:
        shopping = input("Would you like to buy tires with these dimensions? (yes/no) ")
        if shopping.lower() == "yes":
            phone_number = input("Please enter a phone number, and we will contact you at a later time: ")
            print("Have a great day!")
            break
        elif shopping.lower() == "no":
            phone_number = ""
            print("Have a great day!")
            break
        else:
            print("Error: Invalid Argument")

    while True:
        width, aspect_ratio, diameter, volume = main()
        save_data(width, aspect_ratio, diameter, volume, phone_number)
        if not repeat():
            break

if __name__ == "__main__":
    print("Welcome to Tire Volume Calculator")
    print("|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|:|")
    main_loop()
