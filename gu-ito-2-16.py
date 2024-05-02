'''Design a Python program for an e-commerce platform that sells products. Each product on the platform has a name, price, and seller. There are two types of products: new and used. Used products have an additional attribute: condition.

Create classes to represent a Product, NewProduct, and UsedProduct. Use inheritance and the super() function to avoid code duplication. Write a method in each class to print the details of the product.

Sample Input:

Laptop, 1200.99, ElectronicsHub
Smartphone, 450.50, TechResell, Good

Sample Output:

New Product: Laptop, Price: $1200.99, Seller: ElectronicsHub
Used Product: Smartphone, Price: $450.50, Seller: TechResell, Condition: Good

Explanation:

In the sample output, each line represents the details of a product:

The first line is the details of a new product. It's a Laptop with a price of $1200.99 sold by ElectronicsHub.
The second line is the details of a used product. It's a Smartphone with a price of $450.50 sold by TechResell and its condition is Good.
These details are printed by calling the print_details() method of each product object. The method is defined in each class and prints the details specific to that product.

This is an example of single level inheritance, where the NewProduct and UsedProduct classes inherit from a common base class (Product). The base class defines properties and methods common to all products (like name, price, and seller), while the derived classes add properties and methods specific to new and used products. The super() function is used to call a method in the parent class from the child class.

Constraints:

The name of the product and the seller is a string and can contain any printable ASCII characters.
The price of the product is a float and can be any positive number.
The condition of the used product is a string and can contain any printable ASCII characters.'''



class Product:
    def __init__(self, name, price, seller):
        #..... YOUR CODE STARTS HERE .....
        self.name=name
        self.price=price
        self.seller=seller
    
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        pass
    
    
        #..... YOUR CODE ENDS HERE .....

class NewProduct(Product):
    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        return(f"New Product: {self.name}, Price: ${self.price}, Seller: {self.seller}")
    
    
        #..... YOUR CODE ENDS HERE .....

class UsedProduct(Product):
    def __init__(self, name, price, seller, condition):
        #..... YOUR CODE STARTS HERE .....
        super().__init__(name,price,seller)
        self.condition=condition
    
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        return(f"Used Product: {self.name}, Price: ${self.price}, Seller: {self.seller}, Condition: {self.condition}")
    
    
        #..... YOUR CODE ENDS HERE .....

# Get input from the user
product1_info = input().split(", ")
product2_info = input().split(", ")

# Create product objects
product1 = NewProduct(*product1_info)
if len(product2_info) == 4:
    product2 = UsedProduct(*product2_info)
else:
    product2 = None

# Print details
print(product1.print_details())
if product2:
    print(product2.print_details())