# 02 - Functions, *args/**kwargs & Decorators

## Overview
This project covers advanced function concepts in Python:
- Function definitions and calls
- Variable argument handling (*args, **kwargs)
- Decorators and how they work
- Closures and higher-order functions
- Lambda functions and functional programming

## 📋 Topics Covered

### Functions Basics
- Function definition with `def`
- Parameters and arguments
- Return values
- Default parameters
- Keyword arguments
- Docstrings and type hints
- Variable scope (local, global, nonlocal)
- Recursion

### Variable Arguments
- **\*args**: Accept variable number of positional arguments
- **\*\*kwargs**: Accept variable number of keyword arguments
- Combining args and kwargs
- Unpacking with * and **

### Decorators
- What decorators are and why they're useful
- Creating simple decorators
- Using @ syntax
- Decorators with arguments
- Stacking decorators
- Real-world examples (logging, timing, validation)

### Functional Programming
- Lambda functions
- map(), filter(), reduce()
- Higher-order functions
- Closures

## 📁 Files

- `01_basic_functions.py` - Function fundamentals, scope, recursion, lambdas
- `02_args_kwargs.py` - Variable arguments and keyword arguments
- `03_decorators_basics.py` - Introduction to decorators (coming soon)
- `04_decorators_advanced.py` - Advanced decorator patterns (coming soon)

## 🎯 Key Concepts

### Basic Function
```python
def greet(name: str) -> str:
    """A simple greeting function."""
    return f"Hello, {name}!"

print(greet("Alice"))  # Hello, Alice!
```

### *args (Variable Positional Arguments)
```python
def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3, 4))  # 10
print(sum_all(5, 10, 15))    # 30
```

### **kwargs (Variable Keyword Arguments)
```python
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="NYC")
# name: Alice
# age: 30
# city: NYC
```

### Combining *args and **kwargs
```python
def flexible_function(name, *args, **kwargs):
    print(f"Name: {name}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

flexible_function('Alice', 1, 2, 3, color='red', size='large')
```

### Default Parameters
```python
def greet_with_title(name, title="Mr/Ms"):
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")              # Mr/Ms Smith
greet_with_title("Johnson", "Dr")     # Dr Johnson
```

### Lambda Functions
```python
# Simple lambda
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4]
```

### Decorators
```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function call")
        result = func(*args, **kwargs)
        print("After function call")
        return result
    return wrapper

@my_decorator
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Bob")
# Before function call
# Hello, Bob!
# After function call
```

### Recursion
```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

## 🚀 Running the Files

```bash
python 01_basic_functions.py
python 02_args_kwargs.py
python 03_decorators_basics.py
python 04_decorators_advanced.py
```

## ✏️ Exercises

1. Create a function that accepts any number of arguments and returns their product
2. Write a function that accepts keyword arguments for database connection details
3. Create a decorator that measures function execution time
4. Build a decorator that validates input types
5. Create a decorator that retries a function up to 3 times on failure
6. Implement a function that uses both *args and **kwargs effectively
7. Write a recursive function to solve a problem (e.g., Fibonacci)
8. Create a higher-order function that returns another function
9. Use lambda functions with map() and filter()
10. Build a decorator that caches function results (memoization)

## 📚 Resources

- [Python Functions](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [*args and **kwargs](https://docs.python.org/3/tutorial/controlflow.html#more-on-defining-functions)
- [Decorators](https://docs.python.org/3/glossary.html#term-decorator)
- [functools module](https://docs.python.org/3/library/functools.html)
- [Lambda Functions](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions)
- [PEP 362 - Function Signatures](https://www.python.org/dev/peps/pep-0362/)

## 🔗 Next Steps

After mastering this project, move on to:
- **Project 03**: List and Dictionary Comprehensions
- **Project 04**: Generator Expressions
- **Project 05**: Type Hints

## 💡 Tips for Success

- Understand the difference between *args (tuple) and **kwargs (dict)
- Practice using unpacking operators (* and **)
- Experiment with decorators gradually (start simple, build complexity)
- Use type hints for clarity (even though Python is dynamically typed)
- Test your functions with various inputs
- Use docstrings to document your functions
- Consider edge cases (empty args, None values, etc.)

## 🎓 Common Pitfalls

1. **Mutable default arguments**: Avoid `def func(lst=[]):`
   ```python
   # Bad
   def append_item(item, lst=[]):
       lst.append(item)
       return lst
   
   # Good
   def append_item(item, lst=None):
       if lst is None:
       lst = []
       lst.append(item)
       return lst
   ```

2. **Modifying global variables**: Use `global` keyword carefully

3. **Forgetting to return a value**: Functions without explicit return return None

4. **Confusing args order**: *args must come before **kwargs
