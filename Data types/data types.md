## Data Types in Python

### 1. Numeric Types:
   - **int:** Represents integer numbers, positive or negative, without any decimal point.
     Example: `5`, `-10`, `1000`.
   - **float:** Represents floating-point numbers, which include decimal points or use scientific notation.
     Example: `3.14`, `-0.001`, `2.0`, `6.022e23` (scientific notation).
   - **complex:** Represents complex numbers with a real and imaginary part.
     Written in the form `a + bj`, where `a` and `b` are real numbers and `j` represents the square root of -1 (imaginary unit).
     Example: `3 + 4j`, `-2.5 - 1.5j`.
   - **Binary:** Represents numbers in binary (base 2) format using the `0b` prefix.
     Example: `0b1010` (which represents the decimal number `10`), `0b1101` (which represents the decimal number `13`).
   - **Decimal:** Default numeric representation in base 10.
     Example: `10`, `100`, `42`.
   - **Octal:** Represents numbers in octal (base 8) format using the `0o` prefix.
     Example: `0o10` (which represents the decimal number `8`), `0o777` (which represents the decimal number `511`).
   - **Hexadecimal:** Represents numbers in hexadecimal (base 16) format using the `0x` prefix.
     Example: `0x1A` (which represents the decimal number `26`), `0xFF` (which represents the decimal number `255`).

### 2. Sequence Types:
   - **str (string):**
     Represents a sequence of characters enclosed within single, double, or triple quotes.
     Strings are immutable, meaning their contents cannot be changed after creation.
     Example: `'hello'`, `"world"`, `'''multiline string'''`.
   - **list:**
     Represents an ordered collection of items enclosed within square brackets `[]`.
     Lists are mutable, meaning their elements can be modified after creation.
     Example: `[1, 2, 3]`, `['a', 'b', 'c']`.
   - **tuple:**
     Represents an ordered collection of items enclosed within parentheses `()`.
     Tuples are immutable, meaning their elements cannot be changed after creation.
     Example: `(1, 2, 3)`, `('a', 'b', 'c')`.

### 3. Mapping Type:
   - **dict (dictionary):**
     Represents an unordered collection of key-value pairs enclosed within curly braces `{}`.
     Each key-value pair is separated by a colon `:` and keys are unique within a dictionary.
     Example: `{'name': 'John', 'age': 30}`.

### 4. Set Types:
   - **set:**
     Represents an unordered collection of unique items enclosed within curly braces `{}`.
     Sets are mutable but do not allow duplicate elements.
     Example: `{1, 2, 3}`, `{ 'apple', 'banana', 'orange'}`.
   - **frozenset:**
     Similar to sets, but immutable, meaning once created, its elements cannot be changed or modified.

### 5. Boolean Type:
   - **bool:**
     Represents one of two built-in values: `True` or `False`.
     Often used in conditional statements and logical operations.
     Example: `True`, `False`.

### 6. None Type:
   - **None:**
     Represents the absence of a value or a null value.
     Commonly used to signify that a variable or function returns nothing.
     Example: `None`.
