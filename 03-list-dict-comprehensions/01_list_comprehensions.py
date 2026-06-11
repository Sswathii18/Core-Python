"""
01_list_comprehensions.py
Mastering List Comprehensions in Python
"""

print("=" * 60)
print("PYTHON LIST COMPREHENSIONS")
print("=" * 60)

# ============================================================================
# 1. BASIC LIST COMPREHENSION
# ============================================================================
print("\n1. BASIC LIST COMPREHENSION")
print("-" * 60)

# Traditional approach
squares_traditional = []
for num in range(5):
    squares_traditional.append(num ** 2)

print(f"Traditional approach: {squares_traditional}")

# List comprehension approach
squares_comprehension = [num ** 2 for num in range(5)]
print(f"List comprehension:   {squares_comprehension}")

# ============================================================================
# 2. LIST COMPREHENSION WITH CONDITION
# ============================================================================
print("\n\n2. LIST COMPREHENSION WITH CONDITION")
print("-" * 60)

# Even numbers
numbers = range(10)
evens = [num for num in numbers if num % 2 == 0]
print(f"Even numbers from 0-9: {evens}")

# Numbers greater than 5
greater_than_5 = [num for num in range(10) if num > 5]
print(f"Numbers > 5: {greater_than_5}")

# ============================================================================
# 3. LIST COMPREHENSION WITH IF-ELSE
# ============================================================================
print("\n\n3. LIST COMPREHENSION WITH IF-ELSE")
print("-" * 60)

# Convert to 'even' or 'odd'
result = ['even' if num % 2 == 0 else 'odd' for num in range(5)]
print(f"Even/Odd: {result}")

# Multiply by 2 if even, else by 3
modified = [num * 2 if num % 2 == 0 else num * 3 for num in range(5)]
print(f"Modified: {modified}")

# ============================================================================
# 4. LIST COMPREHENSION WITH FUNCTIONS
# ============================================================================
print("\n\n4. LIST COMPREHENSION WITH FUNCTIONS")
print("-" * 60)

def square(x):
    return x ** 2

def is_positive(x):
    return x > 0

# Apply function to each element
numbers = [-2, -1, 0, 1, 2, 3]
squared = [square(num) for num in numbers]
print(f"Original: {numbers}")
print(f"Squared: {squared}")

# Filter with function
positive = [num for num in numbers if is_positive(num)]
print(f"Positive: {positive}")

# ============================================================================
# 5. NESTED LIST COMPREHENSION
# ============================================================================
print("\n\n5. NESTED LIST COMPREHENSION")
print("-" * 60)

# Create matrix (2D list)
matrix = [[i*3 + j for j in range(3)] for i in range(3)]
print(f"Matrix:")
for row in matrix:
    print(f"  {row}")

# Flatten a matrix
flat = [num for row in matrix for num in row]
print(f"Flattened: {flat}")

# ============================================================================
# 6. WORKING WITH STRINGS
# ============================================================================
print("\n\n6. WORKING WITH STRINGS")
print("-" * 60)

# Extract uppercase letters
text = "Hello World Python"
uppercase = [char for char in text if char.isupper()]
print(f"Text: {text}")
print(f"Uppercase letters: {uppercase}")

# Create list from string characters
chars = [char for char in "Python"]
print(f"Characters: {chars}")

# Get words of certain length
words = "The quick brown fox jumps".split()
long_words = [word for word in words if len(word) > 4]
print(f"Long words: {long_words}")

# ============================================================================
# 7. WORKING WITH LISTS
# ============================================================================
print("\n\n7. WORKING WITH LISTS")
print("-" * 60)

# Extract specific indices
data = [10, 20, 30, 40, 50]
every_other = [data[i] for i in range(0, len(data), 2)]
print(f"Original: {data}")
print(f"Every other: {every_other}")

# Remove duplicates while preserving some order
numbers_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique = []
unique_comprehension = [x for x in numbers_with_duplicates if x not in unique and not unique.append(x)]
print(f"With duplicates: {numbers_with_duplicates}")
print(f"Unique (using set): {list(set(numbers_with_duplicates))}")

# ============================================================================
# 8. TRANSFORMING STRINGS IN LIST
# ============================================================================
print("\n\n8. TRANSFORMING STRINGS IN LIST")
print("-" * 60)

words = ['apple', 'banana', 'cherry', 'date']

# Uppercase all
uppercase_words = [word.upper() for word in words]
print(f"Uppercase: {uppercase_words}")

# Add length
with_length = [f"{word} ({len(word)})" for word in words]
print(f"With length: {with_length}")

# Replace character
replaced = [word.replace('a', '@') for word in words]
print(f"Replace 'a' with '@': {replaced}")

# ============================================================================
# 9. MULTIPLE CONDITIONS
# ============================================================================
print("\n\n9. MULTIPLE CONDITIONS")
print("-" * 60)

# Multiple if conditions
numbers = range(20)
result = [num for num in numbers if num % 2 == 0 if num % 3 == 0]
print(f"Numbers divisible by 2 AND 3: {result}")

# Or conditions
result2 = [num for num in range(10) if num % 2 == 0 or num > 7]
print(f"Even numbers OR > 7: {result2}")

# ============================================================================
# 10. NESTED COMPREHENSION WITH CONDITIONS
# ============================================================================
print("\n\n10. NESTED COMPREHENSION WITH CONDITIONS")
print("-" * 60)

# Extract diagonal from matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal = [matrix[i][i] for i in range(len(matrix))]
print(f"Diagonal: {diagonal}")

# Get all pairs of different elements
pairs = [(x, y) for x in range(3) for y in range(3) if x != y]
print(f"Pairs of different elements (0-2): {pairs}")

# ============================================================================
# 11. PERFORMANCE COMPARISON
# ============================================================================
print("\n\n11. PERFORMANCE COMPARISON")
print("-" * 60)

import timeit

# Create large list
size = 1000

# Traditional approach
def traditional():
    result = []
    for i in range(size):
        result.append(i ** 2)
    return result

# Comprehension approach
def comprehension():
    return [i ** 2 for i in range(size)]

# Using map
def map_approach():
    return list(map(lambda x: x ** 2, range(size)))

time_traditional = timeit.timeit(traditional, number=1000)
time_comprehension = timeit.timeit(comprehension, number=1000)
time_map = timeit.timeit(map_approach, number=1000)

print(f"Traditional:   {time_traditional:.6f} seconds")
print(f"Comprehension: {time_comprehension:.6f} seconds")
print(f"Map:           {time_map:.6f} seconds")

# ============================================================================
# 12. PRACTICAL EXAMPLES
# ============================================================================
print("\n\n12. PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Extract file extensions
files = ['document.pdf', 'image.jpg', 'video.mp4', 'archive.zip']
extensions = [file.split('.')[-1] for file in files]
print(f"Files: {files}")
print(f"Extensions: {extensions}")

# Example 2: Convert temperature
celsius = [0, 10, 20, 30, 40]
fahrenheit = [c * 9/5 + 32 for c in celsius]
print(f"\nCelsius: {celsius}")
print(f"Fahrenheit: {fahrenheit}")

# Example 3: Extract keys or values from dict
student_ages = {'Alice': 25, 'Bob': 30, 'Charlie': 22}
names = [name for name in student_ages]
ages = [age for age in student_ages.values()]
print(f"\nStudent dict: {student_ages}")
print(f"Names: {names}")
print(f"Ages: {ages}")

# Example 4: Complex transformation
sentences = ["hello world", "python programming", "list comprehensions"]
title_case = [sentence.title() for sentence in sentences]
print(f"\nOriginal: {sentences}")
print(f"Title case: {title_case}")

# Example 5: Filter and transform combined
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
transformed = [num ** 2 for num in numbers if num % 2 == 0]
print(f"\nNumbers: {numbers}")
print(f"Squares of even numbers: {transformed}")

print("\n" + "=" * 60)
print("END OF LIST COMPREHENSIONS TUTORIAL")
print("=" * 60)
