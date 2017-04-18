"""
A function that returns 'Fizz', 'Buzz', 'FizzBuzz', or 
the argument it receives, all depending on the argument of the function, 
a number that is divisible by, 3, 5, or both 3 and 5, respectively.
"""


def fizz_buzz(n):
    # Check if argument passed is an integer
    if isinstance(n, int):
        # Check if argument is perfectly divisible by 3 and 5
        if n % 3 == 0 and n % 5 == 0:
            return 'FizzBuzz'
        # Check if argument is perfectly divisible by 3
        elif n % 3 == 0:
            return 'Fizz'
        # Check if argument is perfectly divisible by 5
        elif n % 5 == 0:
            return 'Buzz'
        # If not divisible by either 5 or 3, return the argument
        else:
            return n
    # If argument passed is not an integer, raise a TypeError
    else:
        raise TypeError('Argument must be an integer')