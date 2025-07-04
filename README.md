# Module 05 Demonstration Part 1

## Description

Introduction to Python Functions

## Author

Ivan Estropigan

## Demonstration Topics

- (Functions)[]
- Benefits of using functions
- Function definition and syntax
- Function parameters
- Function return values
- Exceptions in functions
- Main guard
- Function Docstrings

## What are Functions?

- Functions are small, reuseable pieces of code that perform specific tasks.
- In Python, you create a function using the def keyword, followed by a unique name, parentheses with any input parameters, and a colon.

- The indented lines following the colon make up the function body.

```cs
def greet(): # No Parameter/Input
    print("Hello World")
```

## Modularity / Reusability

- Functions can be called multiple times from different parts of your code, preventing repetitive code and saving time.
  - Who knows how to do long division?

- Functions improve code maintainability by making it more organized and readable.
- If you need to make changes, you can update the function instead of editing multiple instances of the same code.
  - If you decide to learn a new way to do long division, you only need to change that part one part of your process.

## Debugging / Abstraction

- Functions make it easier to identify and resolve bugs by dividing code into smaller units.
- You can test each function separately to ensure they work correctly before integrating them.
  - If you make mistakes doing long division, you don't need to go searching in the steps for doing multiplication.

- Functions hide the complexity of specific tasks, simplifying code comprehension.
  - How do we calculate exponents?
  - How do we calculate multiplications?
  - How do we calculate addition?
  - Doing this, could toddler calculate x^Y?

- You can execute a task by calling a function without knowing its inner workings.

## Usage

- To define a function in python, you use the def keyword, followed by a unique name, parentheses with any input parameters and a colon.

- The indented lines following the colon make up the function body.
- Edit the file called functions.py
  - This function has no parameters and no return values
  - Code the following function

- Run the application, what happens?

```cs
def greet() -> None: # No Parameter/Input
    """
    print("Hello, World!")
    Returns:
        None aka no value is returned
    """
greet()
```

- Nothing happened, the function has been defined, but does not execute unless it is called.
  - Just because you know how to do long division doesn't mean you'll do it when its not needed

- Code the following below the greet() function (no indenting)
- Run the application
  - Greet displays

- Add a second call to the greet() function
- Run the application
  - Greeting now displays twice

```cs
def greet() -> None: # No Parameter/Input
    """
    print("Hello, World!")
    Returns:
        None aka no value is returned
    """
greet()
greet()

Example 
def greet() -> None: # No Parameter/Input 
    # [greet() code here]
greet()

```

## Parameters

- Parameters are the input passed to a function when it is called.
  - To divide, we need the dividend and the divisor

- You can define a function with one or more parameters by listing them within the parenthese, seperated by commas.

- Code the following function.

```cs
def greet_name(name: str) -> None:
    """
    Prints a greeting which includes the value of the name argument.
    
    Args:
        name (str): The name of the person to greet.
    
    Returns:
        None
    """
    print(f"Hello {name}~")
```

## Multiple Parameters

- We can of course have multiple parameters
- Code the following function.
- Test the function:

```cs
greet_name_age("Annie", 20)
greet_name_age("Bob", 43)

Hello Annie, you are 20 years old!
Hello Bob, you are 43 years old!

```

```cs
def greet_name_age(name: str, age: int)->None:
    """
    Prints a greeting which includes 
    the values of the name and age arguments.
    Args:
        name (str): The name of the person to greet.
        age (int): The age of the person to greet.
    Returns:
        None
    """
    print(f"Hello {name}, you are {age} years old!")

```

## Return Values

- Functions can return a value using the return keyword, followed by the value to be returned
- When a return statement is executed, the function exits, and the returned value is passed back to the caller.

- Code the following function

```cs
def math_operation(operand1: int, operand2: int, operation: str) -> float:
    """
    Returns the result of the specified operation based 
    on the two operands.
    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform.
    Returns:
        result (float): result of the specified operation based 			on the two operands.
    """
    if operation == "+":
        result = operand1 + operand2
    else:
        result = operand1 - operand2    
    return result
```

Test the function:

## Raising exceptions

- Your function must be able to handle all possible inputs
- To account for unexpected inputs, use exceptions

- Modify the math_operation function as follows:

```cs
def math_operation(operand1: int, operand2: int, operation: str) -> float:
    """
    Returns the result of the specified operation based 
    on the two operands.
    Args:
        ………
    Returns:
        ………
    Raises:
        ValueError:  "Invalid operation." When operation is not + or -.
    """
    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation.")
    return result

```
