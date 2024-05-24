'''In an e-commerce application, you have a list of n products. Each product has a unique ID and a price. You need to implement a generator function get_products_in_budget(budget, products) that yields products one by one, sorted by price, until the total price of yielded products exceeds the budget.

Input:

budget: an integer representing the total budget.
products: a list of tuples. Each tuple contains two elements - the first element is the product ID (a string), and the second element is the product price (an integer).
Output:

The function should yield tuples. Each tuple contains two elements - the first element is the product ID (a string), and the second element is the product price (an integer).
Constraints:

1 <= n <= 10^5
1 <= budget <= 10^9
1 <= price <= 10^6
Sample Input:

100
[("p1", 30), ("p2", 50), ("p3", 40), ("p4", 60)]

Sample Output:

('p1', 30)
('p3', 40)

Explanation:

The generator function get_products_in_budget yields products one by one, sorted by price, until the total price of yielded products exceeds the budget. In this case, the products "p1" and "p3" are yielded, with total price 30+40=70, which is the maximum possible total price not exceeding the budget of 100.

This question highlights the importance and performance benefits of generators. Generators allow us to generate as we go along, instead of holding everything in memory. In the context of an e-commerce application, this can be particularly useful when dealing with a large number of products, as it allows us to efficiently process each product one at a time, reducing memory usage.'''




import re

def get_products_in_budget(budget, products):
    #..... YOUR CODE STARTS HERE .....
    
    products.sort(key=lambda x: x[1])
    
    total_price = 0
    
    # Yield products one by one until total price exceeds budget
    for product_id, price in products:
        if total_price + price <= budget:
            yield product_id, price
            total_price += price
        else:
            break    
    
    #..... YOUR CODE ENDS HERE .....
        
def replace_non_alphanumeric(text, replacement=''):
    return re.sub(r'[^a-zA-Z0-9,]', replacement, text)
        
def clean_input(value):
    value = replace_non_alphanumeric(value).split(',')
    
    id, price = list(map(lambda x: x.strip(), value))
    
    return (id, int(price))
    
if __name__ == "__main__":
    budget = int(input())
    products = input()
    
    products = list(map(clean_input, products.strip().replace('[', '').replace(']', '').split('),')))
    
    for product in get_products_in_budget(budget, products):
        print(product)