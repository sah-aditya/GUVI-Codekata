'''In a sports team, each player has a name and a number of goals scored. The number of goals scored should always be a non-negative integer. If a negative value or a non-integer value is assigned to the number of goals, it should be automatically set to 0.

Please write a Python class Player that has name and goals as attributes. Use the property decorator to ensure that goals is always a non-negative integer.

Sample Input 1:

John, 5
10

Sample Output 1:

John
5
10

Sample Input 2:

John, 10
-5

Sample Output 2:

John
10
0

Explanation:

In the sample input, a Player object is created with the name "John" and 5 goals. The goals property is then updated to 10, -5, and "hello". When the goals property is set to a negative value or a non-integer value, the goals.setter method automatically sets goals to 0. This is why the output is 5, 10, 0, 0. This demonstrates how the property decorator can be used to control the values of an attribute.'''




class Player:
    def __init__(self, name, goals=0):
        #..... YOUR CODE STARTS HERE .....
        self._name=name
        self._goals=0
        self.goals = goals
    
    @property
    def goals(self):
        return self._goals
    
        #..... YOUR CODE ENDS HERE .....

    #..... YOUR CODE STARTS HERE .....
    @goals.setter
    def goals(self, value):
        try:
            value = int(value)
            if value < 0:
                self._goals=0
            else:
                self._goals=value
                
        except ValueError:
            self._goals=0
                
                
    @property
    def name(self):
        return self._name
    
    
    #..... YOUR CODE ENDS HERE .....
            
def clean_input(value):
    return str(value.strip())
    
name, goal = map(clean_input, input().strip().split(","))
next_goal = input()

player = Player(name, goal)
print(name)
print(player.goals)
player.goals =next_goal
print(player.goals)