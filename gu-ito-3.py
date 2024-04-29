'''In a scenario where banks need to perform confidential fund or message transfers, each bank may utilize its encryption and decryption techniques. The Reserve Bank provides an interface with method names, leaving the implementation details to the individual banks.

Create an interface BankTransfers.
Add two methods with the following prototypes:
public String encrypt(String a);
public String decrypt(String a);
Create a class ICICI which implements the BankTransfers interface and implements a simple encryption technique.
Create a class HDFC which implements the BankTransfers interface and implements a simple encryption technique.
Encryption techniques used by both banks:
ICICI: Add 1 to the ASCII value of each character and insert the number '1' after every character.
HDFC: Add 1 to the ASCII value of characters at even indices and subtract 1 from the ASCII value of characters at odd indices. Spaces are not encrypted.
The reverse of both techniques will decrypt the message (i.e., original text).

Input:

Bank Type and the message.

Output:

Output the encrypted input.

Sample Input:

1 welcome all

Sample Output:

x1f1m1d1p1n1f1!1b1m1m1'''


# Interface for Bank Transfers
class BankTransfers:
    def encrypt(self, a):
        pass
    
    def decrypt(self, a):
        pass

# ICICI class implementing BankTransfers interface
class ICICI(BankTransfers):
    #..... YOUR CODE STARTS HERE .....

    def encrypt(self,a):
        encrypted_message=""
        for char in a:
            encrypted_message+=chr(ord(char)+1)+"1"
        return encrypted_message
    def decrypt(self,a):
        decrypted_message=""
        for i in range(0,len(a),2):
            decrypted_message+=chr(ord(a[i])-1)
        return decrypted_message
    #..... YOUR CODE ENDS HERE .....

# HDFC class implementing BankTransfers interface
class HDFC(BankTransfers):
    #..... YOUR CODE STARTS HERE .....

    def encrypt(self,a):
        encrypted_message=""
        for i, char in enumerate(a):
            if char!=' ':
                if i%2==0:
                    encrypted_message+=chr(ord(char)+1)
                else:
                    encrypted_message+=chr(ord(char)-1)
            else:
                encrypted_message+=char
        return encrypted_message
    def decrypt(self,a):
        decrypted_message=""
        for i, char in enumerate(a):
            if char!= ' ':
                if i%2==0:
                    decrypted_message+=chr(ord(char)-1)
                else:
                    decrypted_message+=chr(ord(char)+1)
            else:
                decrypted_message+=char
        return decrypted_message

    #..... YOUR CODE ENDS HERE .....

# Main function
def main():
    bank_type, message = input("").split(maxsplit=1)
    bank_type = int(bank_type)
    
    if bank_type == 1:
        bank = ICICI()
    elif bank_type == 2:
        bank = HDFC()
    else:
        print("Invalid bank type")
        return

    encrypted_message = bank.encrypt(message)
    print(encrypted_message)

# Call the main function
if __name__ == "__main__":
    main()
