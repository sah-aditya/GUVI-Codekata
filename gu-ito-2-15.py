'''Design a Python program for a bookstore that uses classes and inheritance. The bookstore sells two types of items: books and magazines. Both books and magazines have a title and a price. However, a book also has an author, while a magazine has an issue number. Create classes to represent both items and use inheritance to avoid code duplication.

Write a method in each class to print the details of the book or magazine. Also, write a method in each class to change the price of the book or magazine.

Sample Input:

The Great Gatsby, F. Scott Fitzgerald, 15.99
Time, 5.99, 23
12.99
4.99

Sample Output:

Book: The Great Gatsby by F. Scott Fitzgerald, priced at $15.99
Magazine: Time, Issue No. 23, priced at $5.99
Book: The Great Gatsby by F. Scott Fitzgerald, priced at $12.99
Magazine: Time, Issue No. 23, priced at $4.99

Explanation:

In the sample output, each line represents the details of an item in the bookstore:

The first line is the details of a book. It's "The Great Gatsby" by F. Scott Fitzgerald, priced at $15.99.
The second line is the details of a magazine. It's "Time", Issue No. 23, priced at $5.99.
The third line is the updated details of the book after changing the price. The price of "The Great Gatsby" has been updated to $12.99.
The fourth line is the updated details of the magazine after changing the price. The price of "Time", Issue No. 23, has been updated to $4.99.
These details are printed by calling the print_details() method of each item object. The method is defined in each class and prints the details specific to that item.

This is an example of single level inheritance, where the Book and Magazine classes inherit from a common base class (Item). The base class defines properties and methods common to all items (like name and price), while the derived classes add properties and methods specific to books and magazines (like author and issue number).

The change_price() method in each class demonstrates the concept of reusability in object-oriented programming. Instead of writing separate functions to change the price of a book and a magazine, we write a single method in the base class (Item) that both Book and Magazine inherit. This allows us to change the price of any item, regardless of whether it's a book or a magazine.

Constraints:

The title of the book or magazine is a string and can contain any printable ASCII characters.
The author of the book is a string and can contain any printable ASCII characters.
The issue number of the magazine is an integer and can be any positive integer.
The price of the book or magazine is a float and can be any positive number.
'''

class Item:
    def __init__(self, title, price):
        #..... YOUR CODE STARTS HERE .....
        self.title=title
        self.price=price
    
    
        #..... YOUR CODE ENDS HERE .....

    def change_price(self, new_price):
        #..... YOUR CODE STARTS HERE .....
        self.new_price=new_price
        self.price=self.new_price
    
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        print(f"Item: {self.title}, priced at ${self.price}")
    
    
        #..... YOUR CODE ENDS HERE .....


class Book(Item):
    def __init__(self, title, author, price):
        #..... YOUR CODE STARTS HERE .....
        super().__init__(title,price)
        self.author=author
    
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        print(f"Book: {self.title} by {self.author}, priced at ${self.price}")
    
    
        #..... YOUR CODE ENDS HERE .....


class Magazine(Item):
    def __init__(self, title, price, issue):
        #..... YOUR CODE STARTS HERE .....
        super().__init__(title,price)
        self.issue=issue
    
    
        #..... YOUR CODE ENDS HERE .....

    def print_details(self):
        #..... YOUR CODE STARTS HERE .....
        print(f"Magazine: {self.title}, Issue No. {self.issue}, priced at ${self.price}")
    
    
        #..... YOUR CODE ENDS HERE .....


def clean_input(ip):
    return str(ip.strip())
    
book_title, book_author, book_price = map(clean_input, input().strip().split(","))
mz_title, mz_price, mz_issue = map(clean_input, input().strip().split(","))

book1 = Book(book_title, book_author, book_price)
magazine1 = Magazine(mz_title, mz_price, mz_issue)

# Printing initial details
book1.print_details()
magazine1.print_details()

# Changing prices
book1.change_price(input())
magazine1.change_price(input())

# Printing updated details
book1.print_details()
magazine1.print_details()