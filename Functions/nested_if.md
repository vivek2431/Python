# Nested If Statements in Python

Nested if statements in Python allow you to have multiple levels of conditional statements within each other. This means you can have an if statement inside another if statement (or inside an if-else statement) to create more complex decision-making structures.

## Basic Syntax

```python
if condition1:
    # Outer if block
    if condition2:
        # Inner if block
        # Code to execute if condition2 is True
    else:
        # Inner else block
        # Code to execute if condition2 is False
else:
    # Outer else block
    # Code to execute if condition1 is False
Example
x = 10
if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")
else:
    print("x is not positive")

In this example:

The outer if statement checks if x is greater than 0.
If x is positive, the inner if statement checks if x is even or odd.
If x is not positive, the outer else statement is executed.
Nested if statements allow you to create more complex logic by branching your code based on multiple conditions. However,
you should use them judiciously to keep your code readable and maintainable. Overly nested structures can become difficult to understand and debug.
