'''You are organizing a marriage function and you have a list of tasks to be done. Each task has a time duration. You want to keep track of how long each task takes. Write a Python decorator time_it that takes a function and prints the time taken by that function. Use this decorator to decorate the function do_task(task), which simulates doing the task by sleeping for the duration of the task.

The output of the do_task function should be in the format: f"{task[0]} took {round(end - start, 2)} seconds"

Input:

task: a tuple. The first element is the task name (a string), and the second element is the task duration in seconds (an integer).
Output:

The function should print the task name and the time taken by the task in the format: f"{task[0]} took {round(end - start, 2)} seconds"
Sample Input:

Decorating the hall, 2

Sample Output:

Decorating the hall took 2.0 seconds

Explanation:

The decorator time_it is used to measure the time taken by the function do_task. The do_task function simulates doing a task by sleeping for the duration of the task. The decorator prints the task name and the time taken by the task. This demonstrates how decorators can be used to modify the behavior of a function, in this case, by adding timing functionality. In the context of organizing a marriage function, this can be useful to keep track of how long each task takes.'''




import time

def time_it(func):
    #..... YOUR CODE STARTS HERE .....
    
    def wrapper(task):
        start_time = time.time()
        result = func(task)
        end_time = time.time()
        duration = end_time - start_time
        print(f"{task[0]} took {round(duration, 2)} seconds")
        return result
    return wrapper    
    
    #..... YOUR CODE ENDS HERE .....

@time_it
def do_task(task):
    #..... YOUR CODE STARTS HERE .....
    
    task_name, task_duration = task
    time.sleep(task_duration)    
    
    #..... YOUR CODE ENDS HERE .....
    
    
if __name__ == "__main__":
    task_name, duration = list(map(lambda x: x.strip(), input().strip().split(',')))
    task = [task_name, int(duration)]
    
    do_task(task)