# 01 - Variables, Types & Control Flow

## Overview
This project covers the fundamental building blocks of Python programming. You'll learn how to:
- Declare and use variables
- Work with different data types
- Use operators
- Control program flow with conditionals and loops

## 📋 Topics Covered

### Variables & Data Types
- **int**: Integer numbers (e.g., 42, -10, 0)
- **float**: Decimal numbers (e.g., 3.14, -2.5)
- **str**: Text/strings (e.g., "Hello", 'Python')
- **bool**: Boolean values (True/False)
- **list**: Ordered, mutable collections
- **tuple**: Ordered, immutable collections
- **dict**: Key-value pairs
- **set**: Unique, unordered collections

### Operators
- **Arithmetic**: +, -, *, /, //, %, **
- **Comparison**: ==, !=, <, >, <=, >=
- **Logical**: and, or, not
- **Assignment**: =, +=, -=, *=, /=
- **Membership**: in, not in
- **Identity**: is, is not
- **Bitwise**: &, |, ^, ~, <<, >>

### Control Flow
- **if-elif-else statements**: Conditional execution
- **for loops**: Iterating over sequences
- **while loops**: Repeating until a condition is false
- **break/continue**: Loop control
- **pass**: Placeholder statement
- **Ternary operator**: Conditional expressions

## 📁 Files

- `01_variables_and_types.py` - Data types, variables, and collections
- `02_operators.py` - All types of operators with examples
- `03_control_flow.py` - Conditionals, loops, and flow control

## 🎯 Key Concepts

### Variables
```python
# Variables are created by assignment
name = "Alice"
age = 25
height = 5.7
is_student = True
```

### Type Checking
```python
# Check the type of a variable
print(type(name))           # <class 'str'>
print(type(age))            # <class 'int'>
print(isinstance(age, int)) # True
```

### Collections
```python
# Lists
numbers = [1, 2, 3, 4, 5]
print(numbers[0])   # 1

# Tuples (immutable)
coords = (10, 20)
print(coords[1])    # 20

# Dictionaries
person = {"name": "Alice", "age": 25}
print(person["name"])  # Alice

# Sets (unique values)
unique = {1, 2, 2, 3}  # {1, 2, 3}
```

### Control Flow
```python
# if-else
if age >= 18:
    print("Adult")
else:
    print("Minor")

# for loop
for i in range(5):
    print(i)

# while loop
while age < 30:
    age += 1

# Ternary operator
status = "Adult" if age >= 18 else "Minor"
```

## 🚀 Running the Files

```bash
python 01_variables_and_types.py
python 02_operators.py
python 03_control_flow.py
```

## ✏️ Exercises

1. Create variables for different data types and print their types
2. Write a program that checks if a number is even or odd
3. Create a list and iterate through it using different loop methods
4. Write a program that prints multiplication table using nested loops
5. Use a dictionary to store student information and retrieve values
6. Create a set and perform set operations (union, intersection)
7. Use list slicing to extract specific portions of data
8. Implement a program using nested loops to create a pattern

## 📚 Resources

- [Python Official Docs - Variables](https://docs.python.org/3/tutorial/introduction.html)
- [Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- [Python Control Flow](https://www.w3schools.com/python/python_conditions.asp)
- [Python Operators](https://www.w3schools.com/python/python_operators.asp)
- [List, Dict, and Set Operations](https://docs.python.org/3/tutorial/datastructures.html)

## 🔗 Next Steps

After mastering this project, move on to:
- **Project 02**: Functions, *args/**kwargs, and Decorators
- **Project 03**: List and Dictionary Comprehensions

## 💡 Tips for Success

- Run each example file and modify the code to experiment
- Try to predict the output before running
- Use the Python interpreter interactively (python3 or ipython)
- Create your own examples to reinforce learning
- Test edge cases (empty lists, None values, etc.)
