'''You are managing an e-commerce website and you have a list of products. Each product is represented as a dictionary with three keys: 'name', 'category', and 'stock'. The 'stock' key represents the number of units of the product available in your inventory. You want to create a dictionary where the keys are the product names and the values are the stock count. Write a Python function product_stock(products) that takes a list of products and returns a dictionary of product names and their stock count. Use a dictionary comprehension to create the dictionary.

Input:

products: a list of dictionaries. Each dictionary represents a product and has three keys: 'name' (a string), 'category' (a string), and 'stock' (an integer).
Output:

The function should return a dictionary where the keys are product names and the values are their stock count.
Sample Input:

[{'name': 'Product 1', 'category': 'Books', 'stock': 20}, {'name': 'Product 2', 'category': 'Electronics', 'stock': 15}, {'name': 'Product 3', 'category': 'Electronics', 'stock': 30}]

Sample Output:

{'Product 1': 20, 'Product 2': 15, 'Product 3': 30}

Explanation:

The dictionary comprehension generates a new dictionary containing product names as keys and their stock count as values. It does this by iterating over each product in the products list and adding an entry to the new dictionary where the key is the product's name and the value is the product's stock count. This demonstrates how dictionary comprehensions can be used to create new dictionaries based on existing lists in Python. In the context of managing an e-commerce website, this can be useful to quickly find the stock count of a product given its name.'''



def product_stock(products):
    #..... YOUR CODE STARTS HERE .....
    
    return {product['name']: product['stock'] for product in products}    
    
    #..... YOUR CODE ENDS HERE .....

products_input = eval(input())

result = product_stock(products_input)
print(result)