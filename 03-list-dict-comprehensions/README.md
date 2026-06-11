# 03 - List & Dict Comprehensions

## Overview
This project teaches you how to write elegant, Pythonic code using comprehensions:
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Nested comprehensions
- Conditional comprehensions

## 📋 Topics Covered

### List Comprehensions
- Basic syntax: `[expression for item in iterable]`
- With conditions: `[expression for item in iterable if condition]`
- Nested comprehensions
- Performance benefits

### Dictionary Comprehensions
- Basic syntax: `{key: value for item in iterable}`
- With conditions
- Swapping keys and values
- Merging dictionaries

### Set Comprehensions
- Creating sets with comprehensions
- Removing duplicates
- Set operations

### Advanced Patterns
- Multiple conditions
- Nested comprehensions
- Combining with functions

## 📁 Files

- `01_list_comprehensions.py` - List comprehension patterns
- `02_dict_comprehensions.py` - Dictionary comprehension patterns
- `03_set_comprehensions.py` - Set comprehension patterns
- `examples/` - Real-world examples

## 🎯 Key Concepts

### List Comprehension
```python
# Traditional approach
squares = []
for num in range(10):
    squares.append(num ** 2)

# List comprehension (cleaner!)
squares = [num ** 2 for num in range(10)]
```

### With Conditions
```python
# Filter even numbers
evens = [num for num in range(20) if num % 2 == 0]

# Transform and filter
result = [x * 2 for x in range(10) if x > 5]
```

### Dictionary Comprehension
```python
# Create dict from lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
d = {k: v for k, v in zip(keys, values)}
# {'a': 1, 'b': 2, 'c': 3}

# Transform dict
d = {k: v ** 2 for k, v in {'a': 2, 'b': 3}.items()}
# {'a': 4, 'b': 9}
```

### Nested Comprehensions
```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## 🚀 Running the Files

```bash
python 01_list_comprehensions.py
python 02_dict_comprehensions.py
python 03_set_comprehensions.py
```

## ✏️ Exercises

1. Create a list of squares for numbers 1-20 using comprehension
2. Filter words longer than 5 characters from a list
3. Create a dictionary mapping words to their lengths
4. Flatten a nested list using comprehension
5. Create a dict with numbers as keys and their squares as values
6. Find all common elements between two lists using comprehension

## 📚 Resources

- [List Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
- [More on Comprehensions](https://docs.python.org/3/tutorial/datastructures.html#dictionaries)
- [PEP 202 - List Comprehensions](https://www.python.org/dev/peps/pep-0202/)
