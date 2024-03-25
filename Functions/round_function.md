# Round Function in Python

The `round()` function in Python is used to round a number to a specified number of decimal places. It takes two parameters: the number to be rounded and the number of decimal places to round to. If the second parameter is not provided, `round()` will round the number to the nearest integer.

## Syntax

```python
round(number, ndigits=None)

Parameters
number: The number to be rounded.
ndigits (optional): The number of decimal places to round to. If not specified, the number will be rounded to the nearest integer.

Returns
The rounded value as a floating-point number.

Examples:
Rounding to the nearest integer:

num = 3.7
rounded_num = round(num)
print(rounded_num)  # Output: 4
Rounding to a specific number of decimal places:

num = 3.14159
rounded_num = round(num, 2)  # Round to 2 decimal places
print(rounded_num)  # Output: 3.14
Rounding to the nearest hundred:

num = 12345
rounded_num = round(num, -2)  # Round to the nearest hundred
print(rounded_num)  # Output: 12300
