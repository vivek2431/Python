# Python Random Module

The `random` module in Python provides functions for generating random numbers. It is commonly used in various applications such as simulations, games, statistical sampling, and cryptography.

## Main Functionalities

### Generating Random Numbers

- `random.random()`: Returns a random floating-point number between 0 and 1.
- `random.randint(a, b)`: Returns a random integer N such that a <= N <= b.
- `random.uniform(a, b)`: Returns a random floating-point number between a and b (inclusive).

### Randomly Choosing Elements

- `random.choice(sequence)`: Returns a random element from a non-empty sequence.
- `random.choices(sequence, weights=None, k=1)`: Returns a list of k elements sampled from the sequence with replacement (optional weights can be provided to bias the selection).
- `random.sample(population, k)`: Returns a list of k unique elements sampled without replacement from the population.

### Shuffling Sequences

- `random.shuffle(sequence)`: Shuffles the elements of a sequence in place.
- `random.sample(population, k)`: Returns a new list containing k elements sampled without replacement from the population.

### Generating Random Sequences

- `random.seed(a=None, version=2)`: Initializes the random number generator with a given seed value (or system time if no seed is provided).
- `random.getstate()`, `random.setstate(state)`: Functions to get and set the internal state of the random number generator, allowing you to save and restore the state for reproducibility.

## Example

```python
import random

# Generate a random floating-point number between 0 and 1
print(random.random())

# Generate a random integer between 1 and 100
print(random.randint(1, 100))

# Choose a random element from a list
colors = ['red', 'green', 'blue', 'yellow']
print(random.choice(colors))

# Shuffle a list in place
random.shuffle(colors)
print(colors)
