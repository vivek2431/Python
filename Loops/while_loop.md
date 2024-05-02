# While Loop in Python

A while loop in Python is a control flow statement that repeatedly executes a block of code as long as a specified condition is true. It continues executing the
block of code until the condition becomes false.

## Syntax

```python
while condition:
    # Code block to execute while condition is True
    # This block can contain one or more statements
`condition`: The expression that is evaluated before each iteration. If it evaluates to True, the loop continues; if it evaluates to False, the loop exits.
The code block under the while statement is executed as long as the condition remains True.
```
### Example 
#### Example of a while loop that counts from 1 to 5
```
n = 1
while n <= 5:
    print(n)
    n += 1
Output :
1
2
3
4
5
```
In this example:

- The variable n is initialized to 1.
- The while loop checks if n is less than or equal to 5.
- Inside the loop, n is printed, and then incremented by 1.
- The loop continues until n is no longer less than or equal to 5.
- While loops are useful when you want to repeat a set of instructions until a specific condition is met. However, it's important to ensure that the condition eventually
  becomes false to avoid infinite loops.


    

