'''You are managing an e-commerce website and you have a list of products. Each product is represented as a dictionary with two keys: 'name' and 'price'. You want to create a list of all products that cost more than $50. Write a Python function expensive_products(products) that takes a list of products and returns a list of the names of products that cost more than $50. Use a list comprehension to create the list.

Input:

products: a list of dictionaries. Each dictionary represents a product and has two keys: 'name' (a string) and 'price' (a float).
Output:

The function should return a list of strings representing the names of products that cost more than $50.
Sample Input:

[{'name': 'Product 1', 'price': 49.99}, {'name': 'Product 2', 'price': 50.01}, {'name': 'Product 3', 'price': 50.00}]

Sample Output:

['Product 2']

Explanation:

The list comprehension generates a new list containing the names of all products that cost more than $50. It does this by iterating over each product in the products list and checking if the product's price is greater than $50. If it is, the product's name is added to the new list. This demonstrates how list comprehensions can be used to create new lists based on existing lists in Python. In the context of managing an e-commerce website, this can be useful to quickly find all products that meet a certain price criterion.'''



import json
from io import StringIO
import re

def expensive_products(products):
    #..... YOUR CODE STARTS HERE .....
    
    return [product['name'] for product in products if product['price'] > 50]    
    
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
    products = convert_to_list_of_dicts(input().strip())
    print(expensive_products(products))