# Conditional Statements in Python

In Python, the `if` statement is used for conditional execution. The basic syntax for the `if` statement is as follows:

```python
if condition:
    # Code block to execute if the condition is True
    statement1
    statement2
    ...
If the condition evaluates to True, the code block inside the if statement is executed. Optionally, you can also include an else statement to provide an alternative code block to execute if the condition is not true:

python
if condition:
    # Code block to execute if the condition is True
    statement1
    statement2
    ...
else:
    # Code block to execute if the condition is False
    statementA
    statementB
    ...
Example
Here's an example of how to use if and else statements in Python:

python
x = 10

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")
Output:

csharp
x is greater than 5
In this example, if x is greater than 5, the code block inside the if statement is executed, printing "x is greater than 5". Otherwise, the code block inside the else statement is executed, printing "x is less than or equal to 5".
