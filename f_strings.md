# F-strings in Python

F-strings (formatted string literals) in Python are a convenient way to format strings dynamically. They allow you to embed expressions inside string literals, 
making string formatting more concise and readable. F-strings are denoted by prefixing the string literal with an 'f' or 'F'.

## Basic Usage:

You can embed expressions within f-strings by placing them inside curly braces `{}`.

```python
name = "Alice"
age = 30
print(f"My name is {name} and I am {age} years old.")
# Output: My name is Alice and I am 30 years old.

Arithmetic Operations:
F-strings support arithmetic operations within expressions.

x = 5
y = 3
print(f"The sum of {x} and {y} is {x + y}.")
# Output: The sum of 5 and 3 is 8.

Formatting Specifiers:
You can specify formatting options within the curly braces to control how values are displayed.

pi = 3.14159
print(f"The value of pi is approximately {pi:.2f}.")
# Output: The value of pi is approximately 3.14.

Accessing Attributes and Methods:
You can access attributes and methods of objects within f-strings.

import datetime

today = datetime.datetime.today()
print(f"Today is {today:%A, %B %d, %Y}.")
# Output: Today is Monday, January 31, 2022.
F-strings provide a concise and powerful way to format strings in Python,
making it easier to write and maintain code that involves string interpolation.
 They were introduced in Python 3.6 and have become a standard feature for string formatting in Python.
