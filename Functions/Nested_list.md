# Nested Lists in Python

In Python, a nested list is a list that contains other lists as its elements. These inner lists can themselves contain other lists, creating a multi-dimensional
structure. Nested lists are useful for representing data in a structured way, such as matrices or tables.

## Example

```python
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
In this example, nested_list is a 2-dimensional list containing three inner lists, each representing a row of a matrix.

Accessing Elements in Nested Lists
You can access elements in a nested list by using multiple index values. The first index specifies the outer list, and the subsequent indices specify the inner lists.

print(nested_list[0])    # Output: [1, 2, 3]
print(nested_list[0][1]) # Output: 2

Iterating Through Nested Lists
You can iterate through a nested list using nested loops.

for row in nested_list:
    for element in row:
        print(element)

Modifying Nested Lists
You can modify elements of a nested list using indexing
nested_list[1][1] = 99
print(nested_list)
# Output: [[1, 2, 3], [4, 99, 6], [7, 8, 9]]

Nested lists are a versatile data structure in Python and are commonly used in applications where data needs to be organized in multiple dimensions.
They can represent complex data structures and are particularly useful for tasks involving matrices, tables,
or hierarchical data.
