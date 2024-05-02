'''You are tasked with creating a Python program to manage the borrowing of resources from a library. The library offers both books and DVDs. Write a Python script that allows users to borrow items from the library. Faculty members can only borrow DVDs, while students can borrow both books and DVDs.

Here are the operations the program should support:

Allow a user to borrow an item from the library.
Display a message indicating whether the borrowing was successful or not, based on the user's status and the type of item they are trying to borrow.
Quit the program.
Ensure the following message formats:

For borrowing a book: Book "{book_title}" successfully borrowed by {self.name}.
For borrowing a DVD by a faculty member: DVD "{title}" successfully borrowed by {self.name}.
For informing a faculty member that they can only borrow DVDs: Faculty members can only borrow DVDs.
Please enter the following details for borrowing:

Name of the borrower
Status of the borrower (faculty/student)
Title of the item to borrow
Sample Input:

Alice
faculty
The Great Gatsby
quit

Sample Output:

Faculty members can only borrow DVDs.
Quitting the program.

Explanation:

Alice, a faculty member, attempts to borrow "The Great Gatsby", which is a book. However, the program informs her that faculty members can only borrow DVDs. Then, the program quits as Alice does not attempt any further operations. Please ensure to include "DVD" in the title if you want to borrow a DVD, as shown in the sample input.

'''




class User:
    def __init__(self, name, user_type):
        #..... YOUR CODE STARTS HERE .....
        self.name=name
        self.user_type=user_type
    
    
        #..... YOUR CODE ENDS HERE .....

    def borrow_book(self, book_title):
        #..... YOUR CODE STARTS HERE .....
        self.book_title=book_title
        return f'Book \"{self.book_title}\" successfully borrowed by {self.name}.'
    
        #..... YOUR CODE ENDS HERE .....

class Faculty(User):
    def __init__(self, name):
        #..... YOUR CODE STARTS HERE .....
        self.name=name
    
    
        #..... YOUR CODE ENDS HERE .....

    def borrow_book(self, title):
        #..... YOUR CODE STARTS HERE .....
        self.title=title
        return f'DVD \"{self.title}\" successfully borrowed by {self.name}.'
    
        #..... YOUR CODE ENDS HERE .....

def main():
    while True:
        name = input()
        user_type = input().lower()
        if user_type == "faculty":
            user = Faculty(name)
        else:
            user = User(name, user_type)

        item_title = input()
        if user_type == "faculty":
            if "DVD" in item_title:
                print(user.borrow_book(item_title))
            else:
                print("Faculty members can only borrow DVDs.")
        else:
            print(user.borrow_book(item_title))

        choice = input().lower()
        if choice != "yes":
            print("Quitting the program.")
            break

if __name__ == "__main__":
    main()