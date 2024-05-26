# Using the `break` Statement in Python

In Python, the `break` statement is used to exit from a loop prematurely. It can be used within `for` loops, `while` loops, and nested loops. When the `break` statement is encountered, the loop stops immediately and control passes to the next statement following the loop.

## Example 1: Using `break` in a `for` loop

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number == 5:
        break
    print(number)

print("Loop ended.")
```
### Output :
```
1
2
3
4
Loop ended.
```
In this example, the loop stops when the value of number becomes 5 because of the break statement.

### Example 2: Using break in a while loop
```
number = 0

while True:
    print(number)
    number += 1
    if number == 5:
        break

print("Loop ended.")
```
### Output :
```
0
1
2
3
4
Loop ended
```
