#Final Project
#Alvin Liu
#CIS 2300 NFA
#May 12,2023

class Converter:
    def __init__(self, Milli, Ounces, Pounds, Gallons):
        self._millimeter = Milli
        self._Ounces = Ounces
        self._Pounds = Pounds
        self._Gallons = Gallons
#setting up the class and the objects for this convertor   
    def set_Cups(self, Milli):
        #self._millimeter = Milli
        if Milli >= 0:
            cups = round(Milli / 236.588, 2)
            print(f"Computing...\nThe quantity in cups is {cups} cups.")
        else:
            print("Please enter a non-negative number:\n")    
    
    def set_grams(self, Ounces):
        #self._Ounces = Ounces
        if Ounces >= 0:
            grams = round(Ounces * 28.3495, 2)
            print(f"Computing...\nThe quantity in grams is {grams} grams.")
        else:
            print("Please enter a non-negative number:\n")
    
    def set_kilograms(self, Pounds):
        #self._Pounds = Pounds
        if Pounds >= 0:
            kilograms = round(Pounds * 0.453592, 2)
            print(f"Computing...\nThe quantity in kilograms is {kilograms} kilograms.")
        else:
            print("Please enter a non-negative number:\n")
    
    def set_Liters(self, Gallons):
        #self._Gallons = Gallons
        if Gallons >= 0:
            liters = round(Gallons * 3.78541, 2)
            print(f"Computing...\nThe quantity in liters is {liters} liters.")
        else:
            print("Please enter a non-negative number:\n")
#Convert all the millimeters, Ounces, Pounds, and Gallons to their respective cups, grams, kilograms, and liters.
#Also rounds the answer to the 2nd decimal place and return a error if the user did not input the correct number.

    
    
    




