# Nested Loop in Python

Nested loops in Python refer to a loop inside another loop. They are used to iterate over multiple sequences or to perform repetitive tasks that require nested iterations. The inner loop runs multiple times for each iteration of the outer loop.

## Example: Printing a Multiplication Table

Here's an example of nested loops to print a multiplication table:

```python
# Example: Nested loop to print a multiplication table
for i in range(1, 6):  # Outer loop for the multiplicand
    for j in range(1, 11):  # Inner loop for the multiplier
        print(i, "x", j, "=", i * j)
    print()  # Add a newline after each row of the table
```

In this example, the outer loop iterates over the multiplicands from 1 to 5, and for each multiplicand, the inner loop iterates over the multipliers from 1 to 10. Inside the inner loop, we print the product of the current multiplicand and multiplier, resulting in a multiplication table.

Nested loops are also commonly used when working with nested data structures like lists of lists or matrices, where you need to iterate over each element in each sublist.

Keep in mind that nesting loops too deeply can lead to code that's hard to read and understand, so use them judiciously.
