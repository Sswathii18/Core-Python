# 04 - Generator Expressions

## Overview
This project explores generators and lazy evaluation:
- Generator functions and yield keyword
- Generator expressions
- Iterator protocol
- Memory efficiency
- Use cases for generators

## 📋 Topics Covered

### Generators Basics
- Generator functions with `yield`
- How generators work
- Lazy evaluation
- Memory efficiency vs lists

### Generator Expressions
- Syntax similar to list comprehensions
- Difference from list comprehensions
- When to use generators

### Iterators
- Iterator protocol
- Creating custom iterators
- `iter()` and `next()` functions

### Advanced Topics
- Sending values to generators
- Generator delegation with `yield from`
- Coroutines

## 📁 Files

- `01_generators_basics.py` - Generator function fundamentals
- `02_generator_expressions.py` - Generator expression syntax
- `03_yield_keyword.py` - Understanding yield
- `examples/` - Practical use cases

## 🎯 Key Concepts

### Generator Function
```python
def count_up_to(n):
    """Generator that yields numbers from 1 to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

# Usage
for num in count_up_to(5):
    print(num)  # Prints 1, 2, 3, 4, 5
```

### Generator Expression
```python
# Similar to list comprehension but with ()
gen = (x ** 2 for x in range(5))

# Iterate through generator
for num in gen:
    print(num)  # Prints 0, 1, 4, 9, 16

# Can only iterate once!
```

### Memory Efficiency
```python
# List: loads all 1 million numbers in memory
numbers_list = [x for x in range(1_000_000)]

# Generator: loads one number at a time
numbers_gen = (x for x in range(1_000_000))

print(sys.getsizeof(numbers_list))   # Large
print(sys.getsizeof(numbers_gen))    # Small (just the generator object)
```

### Yield Keyword
```python
def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

for num in fibonacci(7):
    print(num)  # 0, 1, 1, 2, 3, 5, 8
```

## 🚀 Running the Files

```bash
python 01_generators_basics.py
python 02_generator_expressions.py
python 03_yield_keyword.py
```

## ✏️ Exercises

1. Create a generator for infinite counting
2. Write a generator that reads a large file line by line
3. Create a Fibonacci generator
4. Use generator expression to process a large list
5. Build a generator that filters and transforms data

## 📚 Resources

- [Generators](https://docs.python.org/3/howto/functional.html#generators)
- [yield statement](https://docs.python.org/3/reference/simple_stmts.html#yield)
- [itertools module](https://docs.python.org/3/library/itertools.html)
- [Generator Expressions](https://docs.python.org/3/reference/expressions.html#generator-expressions)
