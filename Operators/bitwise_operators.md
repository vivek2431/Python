# Bitwise Operators in Python

Bitwise operators in Python are used to perform operations on individual bits of integers. Python supports several bitwise operators, including AND, OR, XOR, NOT, left shift, and right shift. Here's an overview of each:

1. **Bitwise AND (`&`):**
   - Performs a bitwise AND operation on corresponding bits of two integers.
   - Example:
     ```python
     a = 5  # 101 in binary
     b = 3  # 011 in binary
     result_and = a & b  # 001 in binary
     print("Bitwise AND:", result_and)  # Output: 1
     ```

2. **Bitwise OR (`|`):**
   - Performs a bitwise OR operation on corresponding bits of two integers.
   - Example:
     ```python
     a = 5  # 101 in binary
     b = 3  # 011 in binary
     result_or = a | b  # 111 in binary
     print("Bitwise OR:", result_or)  # Output: 7
     ```

3. **Bitwise XOR (`^`):**
   - Performs a bitwise XOR (exclusive OR) operation on corresponding bits of two integers.
   - Example:
     ```python
     a = 5  # 101 in binary
     b = 3  # 011 in binary
     result_xor = a ^ b  # 110 in binary
     print("Bitwise XOR:", result_xor)  # Output: 6
     ```

4. **Bitwise NOT (`~`):**
   - Performs a bitwise NOT (complement) operation on an integer, flipping all bits.
   - Example:
     ```python
     a = 5  # 101 in binary
     result_not = ~a  # -(a + 1) = -6
     print("Bitwise NOT:", result_not)  # Output: -6
     ```

5. **Left Shift (`<<`):**
   - Shifts the bits of an integer to the left by a specified number of positions.
   - Example:
     ```python
     a = 5  # 101 in binary
     result_left_shift = a << 1  # 1010 in binary
     print("Left Shift:", result_left_shift)  # Output: 10
     ```

6. **Right Shift (`>>`):**
   - Shifts the bits of an integer to the right by a specified number of positions.
   - Example:
     ```python
     a = 5  # 101 in binary
     result_right_shift = a >> 1  # 10 in binary
     print("Right Shift:", result_right_shift)  # Output: 2
     ```

These bitwise operators are useful for performing low-level bit manipulation operations in Python. They are commonly used in tasks such as cryptography, encoding/decoding, and optimizing algorithms.
