'''You are managing an e-commerce website and you have a list of products. Each product is represented as a dictionary with three keys: 'name', 'category', and 'price'. You want to calculate the total price of all products in a specific category. Write a Python function total_price(products, category) that takes a list of products and a category, and returns the total price of all products in that category. Use the sum function from the built-in Python math module to calculate the total price.

Input:

products: a list of dictionaries. Each dictionary represents a product and has three keys: 'name' (a string), 'category' (a string), and 'price' (a float).
category: a string representing the category of products for which the total price should be calculated.
Output:

The function should return a float representing the total price of all products in the specified category.
Sample Input:

[{'name': 'Product 1', 'category': 'Books', 'price': 19.99}, {'name': 'Product 2', 'category': 'Electronics', 'price': 299.99}, {'name': 'Product 3', 'category': 'Electronics', 'price': 499.99}], 'Electronics'

Sample Output:

799.98

Explanation:

The generator expression generates a sequence of prices for all products in the specified category. It does this by iterating over each product in the products list and checking if the product's category matches the specified category. If it does, the product's price is added to the sequence. The fsum function from the math module then calculates the sum of this sequence, which is the total price of all products in the specified category. This demonstrates how modules and packages can be used in Python to provide additional functionality, such as mathematical operations. In the context of managing an e-commerce website, this can be useful to quickly calculate the total price of all products in a certain category.'''


import json
from io import StringIO
import re
from math import fsum

def total_price(products, category):
    #..... YOUR CODE STARTS HERE .....
    
    return fsum(product['price'] for product in products if product['category'] == category)    
    
    #..... YOUR CODE ENDS HERE .....
    
def convert_to_list_of_dicts(data):
    data_without_brackets = re.sub(r'[\[\]]', '', data).split('},')
    
    lst = []
    
    data = [d + '}' if '}' not in d else d for d in data_without_brackets]

    for d in data:
        if ('{' in d and '}' in d):
            d = d.strip().replace("'", '"')
            lst.append(json.load(StringIO(d)))
        
    return lst
    
if __name__ == "__main__":
    ip = input().strip().replace("],", ']<DIVIDE>')
    products, category = ip.split("<DIVIDE>")
    products = convert_to_list_of_dicts(products)
    category = category.replace("'", '').strip()
    
    print(total_price(products, category))