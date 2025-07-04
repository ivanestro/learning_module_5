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

def math_operation(operand1: int, operand2: int, operation: str) -> float:
    """
    Returns:
        The result of the specified operation based on the two operands.

    Args:
        operand1 (int): The first operand
        operand2 (int): The second operand
        operand (str) The operation to perform.
    
    Returns: 
        result(float): result of the specified operation based on the two operand.

    Raises:
        ValueError: "Invalid operation." When operation is not + or -.
    """
    if operation == "+":
        try:
            result = operand1 + operand2
        except ValueError as e:
            print(e)

    elif operation == "-":
        try:
            result = operand1 - operand2
        except ValueError as e:
            print(e)
    else:
        raise ValueError("Invalid operation.")
    
    return result

#result = math_operation(5,5,"+")
#print(f"The result is: {result}")

try:
    print(math_operation(20,5,"^"))

except ValueError as e:
    print(e)
    
print(greet_name.__doc__)

