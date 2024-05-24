'''You are organizing a marriage function and you have a list of tasks to be done. Each task has a time duration. You want to keep track of the total time taken by all tasks. Write a Python class MarriageFunction with a class method do_task that simulates doing a task and keeps track of the total time taken by all tasks.

Input:

task: a tuple. The first element is the task name (a string), and the second element is the task duration in seconds (an integer).
Output:

The function should print the task name and the time taken by the task in the format: f"{task[0]} took {round(end - start, 2)} seconds
Sample Input:

[("Decorating the hall", 2)]

Sample Output:

Decorating the hall took 2.0 seconds

Explanation:

The class MarriageFunction has a class method do_task which simulates doing a task by sleeping for the duration of the task. The method adds the time taken by the task to the total_duration class variable and prints the task name and the time taken by the task. This demonstrates how class variables can be used to keep track of state across multiple method calls. In the context of organizing a marriage function, this can be useful to keep track of how long all tasks take in total.'''




import time
import re

class MarriageFunction:
    total_duration = 0

    @classmethod
    def do_task(cls, task):
        #..... YOUR CODE STARTS HERE .....
    
        start_time = time.time()
        time.sleep(task[1])
        end_time = time.time()
        duration = end_time - start_time
        cls.total_duration += duration
        print(f"{task[0]} took {round(duration, 2)} seconds")    
    
        #..... YOUR CODE ENDS HERE .....
    
def replace_non_alphanumeric(text, replacement=''):
    return re.sub(r'[^a-zA-Z0-9, ]', replacement, text)
        
def clean_input(value):
    value = replace_non_alphanumeric(value).split(',')
    
    id, price = list(map(lambda x: x.strip(), value))
    
    return (id, int(price))
    
if __name__ == "__main__":
    tasks = input()
    
    tasks = list(map(clean_input, tasks.strip().replace('[', '').replace(']', '').split('),')))
    
    for task in tasks:
       MarriageFunction.do_task(task)