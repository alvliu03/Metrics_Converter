#Final Project
#Alvin Liu
#CIS 2300 NFA
#May 12,2023

import Liu_metrics
#Needed to Import Liu_Metrics so we can use the converter
def main():
    name = input("Please enter your name:\n")
    print(f"Welcome {name} to the Metrics Converter Application.")
    converter = Liu_metrics.Converter(0, 0, 0, 0)
    #Ask for the User's name and set all the objects in the Liu_Metrics to zero.
    while True:
        print("Choice 1: Convert Milliliters to Cups.")
        print("Choice 2: Convert Ounces to Grams.")
        print("Choice 3: Convert Pounds to Kilograms.")
        print("Choice 4: Convert Gallons to Liters.")
        print("Choice 5: Exit the Program")
        Choice = input("Enter your choice from 1-5:\n")
        if Choice == "1":
            Milli = float(input("Please enter your quantity in Milliliters:\n"))
            converter.set_Cups(Milli)
        elif Choice == "2":
            Ounces = float(input("Please enter your quantity in Ounces:\n"))
            converter.set_grams(Ounces)
        elif Choice == "3":
            Pounds = float(input("Please enter your quantity in Pounds:\n"))
            converter.set_kilograms(Pounds)
        elif Choice == "4":
            Gallons = float(input("Please enter your quantity in Gallons:\n"))
            converter.set_Liters(Gallons)
        elif Choice == "5":
            print("Exiting...\nThank you for using the Metrics Converter Application")
            break
        else:
            print("That is not an option. Please try again.")
    #Will keep asking the user for choices to convert until they hit 5.
    #See the choices that the user selected and using the Converter from Liu_Metrics, it will convert the units.
    #Also implemented a way to ensure that we only get the input 1-5 from the user.


main()