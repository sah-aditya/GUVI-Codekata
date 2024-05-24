'''You are given a string that represents a list of movies and their release years. The format of the string is "<movie title> (<release year>)". Write a Python function get_movies(data) that takes this string and returns a list of tuples where each tuple contains the movie title and the release year. Use regular expressions to parse the data.

Input:

data: a string representing a list of movies and their release years.
Output:

The function should return a list of tuples where each tuple contains a movie title and the release year.
Sample Input:

The Shawshank Redemption (1994), The Godfather (1972), The Dark Knight (2008)

Sample Output:

[('The Shawshank Redemption', '1994'), ('The Godfather', '1972'), ('The Dark Knight', '2008')]

Explanation:

The re.findall function applies the regular expression pattern to the data string and returns a list of tuples where each tuple contains the movie title and the release year.'''


import re

def get_movies(data):
    #..... YOUR CODE STARTS HERE .....
    
    # Define the regular expression pattern
    pattern = r'([\w\s]+) \((\d{4})\)'

    # Find all matches using the pattern
    matches = re.findall(pattern, data)

    # Create a list of tuples from the matches
    movies = [(title.strip(), year) for title, year in matches]

    return movies    
    
    #..... YOUR CODE ENDS HERE .....
    
if __name__ == "__main__":
    data = input().strip()
    print(get_movies(data))