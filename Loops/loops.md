# Loops in Python

Loops in Python are used to repeatedly execute a block of code until a certain condition is met. There are two main types of loops in Python: `for` loops and `while` loops.

## `for` Loops

A `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute the block of code for each element in the sequence.

### Syntax:
```python
for item in sequence:
    # Code block to execute for each item
```
### Example:
```
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```
## while Loops
A while loop is used to repeatedly execute a block of code as long as a specified condition is true.
```
while condition:
    # Code block to execute as long as condition is true
```
### Example:
```
i = 0
while i < 5:
    print(i)
    i += 1
```
## Loop Control Statements
Python provides loop control statements to change the execution flow of loops.

- break Statement: Used to exit the loop prematurely.
- continue Statement: Used to skip the current iteration of the loop.
- else Clause: Executed when the loop terminates naturally.

### Example: 
```
for i in range(5):
    if i == 3:
        continue
    print(i)
else:
    print("Loop ended successfully")
```
## Nested Loops
Python allows you to nest loops within each other to perform more complex iterations.

### Example:
```
for i in range(3):
    for j in range(2):
        print(i, j)
```
## Conclusion
Loops are fundamental constructs in Python programming that enable you to automate repetitive tasks and iterate over collections of data. 
They provide flexibility and efficiency in writing code to solve various problems.
