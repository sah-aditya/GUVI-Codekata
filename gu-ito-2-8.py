'''You are developing a stock management system for a market. The system has a function get_stock(item: str) -> int that takes an item name as input and returns the quantity of that item in stock.

The market has the following items in stock:

"Apples" - 50
"Oranges" - 30
"Grapes" - 0
However, not all items are available in the market at all times. If an item is not available, the function should raise a custom exception ItemNotFoundError with a message "Item not found".

Write a Python function handle_stock_request(item: str) -> str that calls get_stock(item: str) -> int and handles any ItemNotFoundError that might be raised. The function should return a string message about the status of the request.

If the item is found and the stock is greater than 0, the function should return a message in the following format: "Stock for {item}: {stock}". If the item is not found or the stock is 0, it should return the message "Item not found".

Constraints:

Item is a string.
You can't install any external libraries.
Sample Input:

Apples

Sample Output:

Stock for Apples: 50

Explanation:

In the sample outputs, the message is returned when the item is found in the market and the stock is greater than 0. The stock quantity of the item is displayed in the message. This is done by catching the stock quantity returned by the get_stock function in a try block.'''




class ItemNotFoundError(Exception):
    pass

def get_stock(item):
    stock = {
        "Apples": 50,
        "Oranges": 30,
        "Grapes": 0,
    }
    if item in stock:
        return stock[item]
    else:
        raise ItemNotFoundError("Item not found")

def handle_stock_request(item):
    #..... YOUR CODE STARTS HERE .....
    try:
        stock = get_stock(item)
        return f"Stock for {item}: {stock}"
    except ItemNotFoundError:
        return "Item not found"
    
    
    
    #..... YOUR CODE ENDS HERE .....

user_input = input()

print(handle_stock_request(user_input))