# Identity Operators in Python

Identity operators in Python are used to compare the memory locations of two objects. Python provides two identity operators: `is` and `is not`. Here's an overview of each:

1. **Identity Operator `is`:**
   - Returns `True` if both operands refer to the same object (have the same memory address), otherwise returns `False`.
   - Example:
     ```python
     x = [1, 2, 3]
     y = [1, 2, 3]
     z = x

     print(x is y)  # Output: False (x and y are different objects)
     print(x is z)  # Output: True (x and z refer to the same object)
     ```

2. **Identity Operator `is not`:**
   - Returns `True` if both operands refer to different objects (have different memory addresses), otherwise returns `False`.
   - Example:
     ```python
     x = [1, 2, 3]
     y = [1, 2, 3]
     z = x

     print(x is not y)  # Output: True (x and y are different objects)
     print(x is not z)  # Output: False (x and z refer to the same object)
     ```

Identity operators are used to compare objects based on their identity rather than their values. They are typically used when comparing mutable objects like lists, dictionaries, and sets, to determine whether two variables reference the same object or not.
