'''You're developing a Python program for a virtual pet simulation game. The game features various types of pets, each with its own unique abilities and needs. You need to implement a system to manage different types of pets and their actions. The program should support pets such as cats, dogs, and birds.

Write a Python script that demonstrates method overloading in the context of different pet classes. Your program should accomplish the following tasks:

Define a base class called Pet.
Implement different subclasses for various types of pets, such as Cat, Dog, and Bird.
Each pet class should have methods to perform actions such as eating, sleeping, and making sounds.
Demonstrate method overloading by implementing different versions of the eat(), sleep(), and make_sound() methods for each pet class.
Additionally, integrate some unique behaviors for each type of pet:

Cats should be able to purr when making a sound.
Dogs should be able to wag their tails when making a sound.
Birds should be able to chirp when making a sound.
Ensure the following operations can be performed:

Feed a pet and display a message indicating it's eating.
Put a pet to sleep and display a message indicating it's sleeping.
Prompt a pet to make a sound and display the appropriate message based on its type.
Your program should continuously prompt the user for pet actions until the "quit" command is entered.

Provide appropriate error handling for invalid inputs. Display a message in the following format for invalid inputs: "Invalid input. Please enter a valid action (feed/sleep/make_sound/quit)."

Sample Input:

cat
eat
dog
make_sound
bird
sleep
quit

Sample Output:

Cat is eating.
Dog is wagging its tail.
Bird is sleeping.
Quitting the program.

Explanation:

The user selects a pet and an action to perform.
The program executes the action based on the selected pet type and displays an appropriate message.
The process continues until the user enters "quit." If the user enters an invalid action, an appropriate error message is displayed.'''



class Pet:
    #..... YOUR CODE STARTS HERE .....

    def eat(self):
        pass
    def sleep(self):
        pass
    def make_sound(self):
        pass
    
    #..... YOUR CODE ENDS HERE .....


class Cat(Pet):
    #..... YOUR CODE STARTS HERE .....
    def eat(self):
        print("Cat is eating.")
    def sleep(self):
        print("Cat is sleeping.")
    def make_sound(self):
        print("Cat is purring.")
    
    
    #..... YOUR CODE ENDS HERE .....

class Dog(Pet):
    #..... YOUR CODE STARTS HERE .....
    def eat(self):
        print("Dog is eating.")
    def sleep(self):
        print("Dog is sleeping.")
    def make_sound(self):
        print("Dog is wagging its tail.")
    
    
    #..... YOUR CODE ENDS HERE .....

class Bird(Pet):
    #..... YOUR CODE STARTS HERE .....
    def eat(self):
        print("Bird is eating.")
    def sleep(self):
        print("Bird is sleeping.")
    def make_sound(self):
        print("Bird is chirping.")
    
    
    #..... YOUR CODE ENDS HERE .....

def main():
    while True:
        pet_type = input("").lower()
        if pet_type == 'quit':
            print("Quitting the program.")
            break
        elif pet_type not in ['cat', 'dog', 'bird']:
            print("Invalid input. Please enter a valid pet type (cat/dog/bird).")
            continue

        pet_action = input("").lower()
        if pet_action == 'quit':
            print("Quitting the program.")
            break
        elif pet_action not in ['eat', 'sleep', 'make_sound']:
            print("Invalid input. Please enter a valid action (eat/sleep/make_sound/quit).")
            continue

        if pet_type == 'cat':
            cat = Cat()
            if pet_action == 'eat':
                cat.eat()  # Output: "Cat is eating."
            elif pet_action == 'sleep':
                cat.sleep()  # Output: "Cat is sleeping."
            elif pet_action == 'make_sound':
                cat.make_sound()  # Output: "Cat is purring."
        elif pet_type == 'dog':
            dog = Dog()
            if pet_action == 'eat':
                dog.eat()  # Output: "Dog is eating."
            elif pet_action == 'sleep':
                dog.sleep()  # Output: "Dog is sleeping."
            elif pet_action == 'make_sound':
                dog.make_sound()  # Output: "Dog is wagging its tail."
        elif pet_type == 'bird':
            bird = Bird()
            if pet_action == 'eat':
                bird.eat()  # Output: "Bird is eating."
            elif pet_action == 'sleep':
                bird.sleep()  # Output: "Bird is sleeping."
            elif pet_action == 'make_sound':
                bird.make_sound()  # Output: "Bird is chirping."

if __name__ == "__main__":
    main()