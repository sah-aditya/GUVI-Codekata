'''You are developing a book management system for a bookstore. The system has a function get_book_details(isbn: str) -> dict that takes an ISBN number as input and returns a dictionary with book details. The dictionary contains the following keys: 'title', 'author', 'price', and 'quantity'.

The bookstore has the following books:

"Python Programming" by John Doe, ISBN: "1234567890", Price: 500, Quantity: 10
"Data Structures and Algorithms" by Jane Doe, ISBN: "9876543210", Price: 600, Quantity: 5
"Machine Learning" by Sam Smith, ISBN: "1111111111", Price: 700, Quantity: 2
However, not all books are available in the store at all times. If a book is not available, the function should raise a ValueError with a message "Book not found".

Write a Python function handle_book_request(isbn: str) -> str that calls get_book_details(isbn: str) -> dict and handles any ValueError that might be raised. The function should return a string message about the status of the request.

If the book is found, the function should return a message in the following format: "Book found: {title} by {author}. Price: {price}, Quantity: {quantity}". If the book is not found, it should return the message "Book not found".

Constraints:

ISBN is a string of length 10 or 13.
The title, author are strings and price, quantity are integers.
You can't install any external libraries.
Sample Input:

1234567890

Sample Output:

Book found: Python Programming by John Doe. Price: 500, Quantity: 10

Explanation:

In the sample output, that message is returned when the book is found in the bookstore. The details of the book, including the title, author, price, and quantity, are displayed in the message. This is done by catching the book details returned by the get_book_details function in a try block.

A message, "Book not found", is returned If the book is not found in the bookstore. This happens when the get_book_details function raises a ValueError. In the except block, this error is caught and the error message is returned. This demonstrates how error handling works in Python - when an error occurs, instead of the program crashing, the error is caught and handled gracefully. In this case, a meaningful message is returned to the user. This is a key aspect of robust software design.'''


def get_book_details(isbn):
    books = {
        "1234567890": {"title": "Python Programming", "author": "John Doe", "price": 500, "quantity": 10},
        "9876543210": {"title": "Data Structures and Algorithms", "author": "Jane Doe", "price": 600, "quantity": 5},
        "1111111111": {"title": "Machine Learning", "author": "Sam Smith", "price": 700, "quantity": 2},
    }
    if isbn in books:
        return books[isbn]
    else:
        raise ValueError("Book not found")

def handle_book_request(isbn):
    #..... YOUR CODE STARTS HERE .....
    try:
        book =  get_book_details(isbn)
        return f"Book found: {book['title']} by {book['author']}. Price: {book['price']}, Quantity: {book['quantity']}"
    except ValueError:
        return "Book not found"
    
    #..... YOUR CODE ENDS HERE .....

isbn = input()
response = handle_book_request(isbn)
print(response)