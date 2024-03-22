# Membership Operators in Python

Membership operators in Python are used to test whether a value or variable is found within a sequence (such as a string, list, tuple, or set). Python provides two membership operators: `in` and `not in`. Here's an overview of each:

1. **Membership Operator `in`:**
   - Returns `True` if the specified value is found in the specified sequence, otherwise returns `False`.
   - Example:
     ```python
     sequence = [1, 2, 3, 4, 5]
     print(3 in sequence)  # Output: True
     ```

2. **Membership Operator `not in`:**
   - Returns `True` if the specified value is not found in the specified sequence, otherwise returns `False`.
   - Example:
     ```python
     sequence = [1, 2, 3, 4, 5]
     print(6 not in sequence)  # Output: True
     ```

Membership operators are commonly used in conditional statements (`if`, `elif`, `else`) and looping constructs (`for` loops) to check for the presence or absence of a value within a sequence. They provide a convenient way to test for membership without needing to manually iterate over the sequence.
