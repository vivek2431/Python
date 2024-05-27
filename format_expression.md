# Python String Formatting

This guide covers various methods of formatting strings in Python. 

## 1. Using the `%` Operator (Old Style)
The `%` operator is an older way of formatting strings. It works similarly to C's `printf`.

```python
name = "Alice"
age = 30
formatted_string = "Hello, %s. You are %d years old." % (name, age)
print(formatted_string)
```
## 2. Using str.format() (New Style)

The `str.format()` method provides more functionality and is generally preferred over the % operator.
```
name = "Bob"
age = 25
formatted_string = "Hello, {}. You are {} years old.".format(name, age)
print(formatted_string)
```
## 3. Using f-Strings

f-Strings (formatted string literals) are a more concise and readable way to format strings, introduced in Python 3.6.
```
name = "Charlie"
age = 20
formatted_string = f"Hello, {name}. You are {age} years old."
print(formatted_string)
```
## 4. Advanced Formatting Options

With `str.format()`
You can use more advanced formatting with the `str.format()` method:
```
value = 1234.56789
formatted_string = "The value is {:.2f}".format(value)
print(formatted_string)  # The value is 1234.57

formatted_string = "The value is {:,.2f}".format(value)
print(formatted_string)  # The value is 1,234.57
```
## 5.With f-Strings
f-Strings also support advanced formatting options:
```
value = 1234.56789
formatted_string = f"The value is {value:.2f}"
print(formatted_string)  # The value is 1234.57

formatted_string = f"The value is {value:,.2f}"
print(formatted_string)  # The value is 1,234.57
```
## 6. Formatting Dictionaries and Lists
You can format dictionaries and lists using these methods as well:
```
person = {"name": "David", "age": 28}
formatted_string = "Name: {name}, Age: {age}".format(**person)
print(formatted_string)
```
## 7. With f-Strings
```
person = {"name": "Eve", "age": 32}
formatted_string = f"Name: {person['name']}, Age: {person['age']}"
print(formatted_string)
```

## Conclusion:
- Each method has its own advantages:
- The % operator is useful for older code bases.
- `str.format()` is more powerful and flexible.
- `f-Strings` are the most readable and concise for Python 3.6 and newer.
