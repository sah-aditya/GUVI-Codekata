'''You are managing a bank's software system. You want to calculate the monthly interest for a given principal amount, rate of interest, and time period. Write a Python function calculate_interest(principal, rate, time) to calculate and return the monthly interest.

Input:

principal: a float representing the principal amount.
rate: a float representing the annual rate of interest in percentage.
time: an integer representing the time period in months.
Output:

The function should return a float representing the monthly interest.
Sample Input:

1000.0, 5, 12

Sample Output:

50.0

Explanation:

The calculate_interest function takes three parameters: principal, rate, and time, representing the principal amount, annual rate of interest (in percentage), and time period (in months) respectively. Inside the function, it first converts the annual rate to a monthly rate by dividing it by 100 and then by 12 (since there are 12 months in a year).
Then, it calculates the monthly interest by multiplying the principal amount with the monthly rate and the time period.'''



def calculate_interest(principal, rate, time):
    #..... YOUR CODE STARTS HERE .....
    
    monthly_rate = rate / (100 * 12)  # Convert annual rate to monthly rate
    monthly_interest = principal * monthly_rate * time
    return monthly_interest    
    
    #..... YOUR CODE ENDS HERE .....


if __name__ == "__main__":
    principal, rate, time = list(map(float, input().strip().split(',')))
    
    # Calculate and print monthly interest
    print(calculate_interest(principal, rate, time))