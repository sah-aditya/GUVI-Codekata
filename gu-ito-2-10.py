'''In the sample output, each line represents the details of an electronic device:

The first line is the details of a mobile. It's a Samsung Galaxy S21 with a price of $799.99 and a screen size of 6.2 inches.
The second line is the details of a laptop. It's a Dell XPS 13 with a price of $999.99 and a screen resolution of 1920 x 1080.
These details are printed by calling the print_details() method of each device object. The method is defined in each class and prints the details specific to that device.

This is an example of hierarchical inheritance, where the Mobile and Laptop classes inherit from a common base class (ElectronicDevice). The base class defines properties and methods common to all electronic devices (like name and price), while the derived classes add properties and methods specific to mobiles and laptops (like screen_size and screen_resolution).

Constraints:

The name of the mobile or laptop is a string and can contain any printable ASCII characters.
The price of the mobile or laptop is a float and can be any positive number.
The screen size of the mobile is a string and can contain any printable ASCII characters.
The screen resolution of the laptop is a string and can contain any printable ASCII characters.
'''

class ElectronicDevice:
    def __init__(self, name, price):
        #..... YOUR CODE STARTS HERE .....
        self.name=name
        self.price=price
    
    
        #..... YOUR CODE ENDS HERE .....

class Mobile(ElectronicDevice):
    def __init__(self, name, price, screen_size):
        #..... YOUR CODE STARTS HERE .....
        super().__init__(name,price)
        self.screen_size=screen_size
    
    
        #..... YOUR CODE ENDS HERE .....
        
    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        return(f"Mobile: {self.name}, Price: ${self.price}, Screen Size: {self.screen_size}" )
    
    
        #..... YOUR CODE ENDS HERE .....

class Laptop(ElectronicDevice):
    def __init__(self, name, price, screen_resolution):
        #..... YOUR CODE STARTS HERE .....
        super().__init__(name,price)
        self.screen_resolution=screen_resolution
    
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        return(f"Laptop: {self.name}, Price: ${self.price}, Screen Resolution: {self.screen_resolution}")
    
    
        #..... YOUR CODE ENDS HERE .....

# Get sample input from the user
mobile_input = input().split(", ")
laptop_input = input().split(", ")

# Create objects
mobile = Mobile(*mobile_input)
laptop = Laptop(*laptop_input)

# Print details
print(mobile.print_details())
print(laptop.print_details())