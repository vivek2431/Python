# Dictionary in Python

A dictionary in Python is a mutable, unordered collection of key-value pairs. It allows you to store and retrieve data efficiently using keys. Each key in a dictionary must be unique and immutable, typically strings or numbers, while values can be of any data type and can be mutable or immutable. 

## Basic Usage

Dictionaries are defined using curly braces `{}`, with key-value pairs separated by commas and each key separated from its corresponding value by a colon `:`.

```python
# Creating a dictionary
my_dict = {"apple": 2, "banana": 3, "orange": 1}

# Accessing values using keys
print(my_dict["apple"])  # Output: 2

# Adding a new key-value pair
my_dict["grape"] = 4

# Modifying a value
my_dict["banana"] = 5

# Deleting a key-value pair
del my_dict["orange"]

# Checking if a key exists
if "banana" in my_dict:
    print("Yes, 'banana' is in the dictionary.")
```
## Applications
Dictionaries offer a very flexible way to organize and manipulate data, making them one of the most useful data structures in Python. They're commonly used in various applications, such as representing JSON data,
storing configuration settings, or mapping unique identifiers to values.

## Operations
- len(dictionary) - Returns the number of items in a dictionary.

- for key, in dictionary - Iterates over each key in a dictionary.

- for key, value in dictionary.items() - Iterates over each key,value pair in a dictionary.

- if key in dictionary - Checks whether a key is in a dictionary.

- dictionary[key] - Accesses a value using the associated key from a dictionary.

- dictionary[key] = value - Sets a value associated with a key.

- del dictionary[key] - Removes a value using the associated key from a dictionary.

## Methods
- dictionary.get(key, default) - Returns the value corresponding to a key, or the default value if the specified key is not present.

- dictionary.keys() - Returns a sequence containing the keys in a dictionary.

- dictionary.values() - Returns a sequence containing the values in a dictionary.

- dictionary[key].append(value) - Appends a new value for an existing key.

- dictionary.update(other_dictionary) - Updates a dictionary with the items from another dictionary. Existing entries are updated; new 
 entries are added.

- dictionary.clear() - Deletes all items from a dictionary.

- dictionary.copy() - Makes a copy of a dictionary.
