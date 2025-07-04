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
