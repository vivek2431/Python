# Nested if-else Statements in Python

Nested `if`-`else` statements in Python allow for more complex conditional logic by nesting one or more `if`-`else` statements within each other. Here's the basic syntax:

```python
if condition1:
    if condition2:
        # Code block to execute if both condition1 and condition2 are True
        statement1
        statement2
        ...
    else:
        # Code block to execute if condition1 is True but condition2 is False
        statementA
        statementB
        ...
else:
    # Code block to execute if condition1 is False
    statementX
    statementY
    ...
You can nest if-else statements to any level of depth as needed to express the desired logic.

Example
Here's an example of a nested if-else statement in Python:

x = 10
y = 20

if x > 5:
    if y > 15:
        print("x is greater than 5 and y is greater than 15")
    else:
        print("x is greater than 5 but y is not greater than 15")
else:
    print("x is not greater than 5")
Output:

csharp

x is greater than 5 and y is greater than 15
In this example, the nested if-else statement first checks if x is greater than 5. If it is, it checks if y is greater than 15.
If both conditions are true, it prints "x is greater than 5 and y is greater than 15". If x is greater than 5 but y is not greater than 15,
it prints "x is greater than 5 but y is not greater than 15". If x is not greater than 5, it prints "x is not greater than 5".
