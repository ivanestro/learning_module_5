"""
Description: Module 05 demonstration: Functions
Author: {student name}
Date: {current date}
Usage: To run individual functions, place a function 
call within the main guard.
"""

def greet_name(name: str, age: int) -> None: # No Parameter/Input
    """
    Description:
        prints a greet message to the console.

    Returns:
        None aka no value is returned
    
    Arguments:
        name(str): The name of the person to greet.
        age(int): The age of a person to greet.
    """
    print(f"Hello, {name}, you are {age} years young!")

greet_name("Ivan", 24)
print(greet_name.__doc__)
#print(print.__doc__)
