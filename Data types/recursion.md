# Recursion in Python

Recursion in Python refers to the concept of a function calling itself directly or indirectly in order to solve a problem. 
Recursion is a powerful technique used in programming where a function solves a problem by dividing it into smaller instances
of the same problem until a base case is reached. Once the base case is reached, the function returns its result, 
and the recursion "unwinds" back to the original call.

## Example: Factorial Calculation

Here's an example of a recursive function to calculate the factorial of a number:

```python
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    # Recursive case: multiply n by factorial of n-1
    else:
        return n * factorial(n - 1)

# Example usage
print(factorial(5))  # Output: 120
```
In this example, the `factorial()` function calls itself with a smaller argument `(n - 1)` until it reaches the base case `(n == 0 or n == 1)`. 
Then, it returns 1, and the results are multiplied back up the call stack.
Recursion can be a powerful tool, but it's essential to ensure that the base case is reachable and that the recursive calls 
eventually terminate. Otherwise, the function will continue to call itself indefinitely, resulting in a stack overflow error.
