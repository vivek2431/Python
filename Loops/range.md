# Range Function in Python

In Python, the `range()` function is used to generate a sequence of numbers. It is commonly used in for loops to iterate a specific number of times.

## Syntax

```python
range(start, stop, step)
```
- ### start: The starting value of the sequence (inclusive). If not specified, it defaults to 0.
- ### stop: The ending value of the sequence (exclusive). This is a required argument.
- ### step: The step or increment between each number in the sequence. If not specified, it defaults to 1.

### Example
#### Basic Usage
```
# Iterate over a sequence of numbers from 0 to 4 (exclusive)
for i in range(5):
    print(i)
```
#### Output:
```
0
1
2
3
4
```
#### Specifying Start and Step
```
# Iterate over a sequence of numbers from 2 to 10 (exclusive) with a step of 2
for i in range(2, 11, 2):
    print(i)
```
#### Output:
```
2
4
6
8
10
```
