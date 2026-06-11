"""
02_dict_comprehensions.py
Mastering Dictionary Comprehensions in Python
"""

print("=" * 60)
print("PYTHON DICTIONARY COMPREHENSIONS")
print("=" * 60)

# ============================================================================
# 1. BASIC DICT COMPREHENSION
# ============================================================================
print("\n1. BASIC DICT COMPREHENSION")
print("-" * 60)

# Traditional approach
squares_dict_traditional = {}
for num in range(5):
    squares_dict_traditional[num] = num ** 2

print(f"Traditional approach: {squares_dict_traditional}")

# Dict comprehension approach
squares_dict = {num: num ** 2 for num in range(5)}
print(f"Dict comprehension:   {squares_dict}")

# ============================================================================
# 2. DICT COMPREHENSION WITH CONDITION
# ============================================================================
print("\n\n2. DICT COMPREHENSION WITH CONDITION")
print("-" * 60)

# Only even numbers
even_squares = {num: num ** 2 for num in range(10) if num % 2 == 0}
print(f"Even numbers squared: {even_squares}")

# Numbers and their type
mixed = {num: ('even' if num % 2 == 0 else 'odd') for num in range(6)}
print(f"Number types: {mixed}")

# ============================================================================
# 3. CREATING DICT FROM TWO LISTS
# ============================================================================
print("\n\n3. CREATING DICT FROM TWO LISTS")
print("-" * 60)

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

# Using zip
result_dict = {k: v for k, v in zip(keys, values)}
print(f"Keys: {keys}")
print(f"Values: {values}")
print(f"Combined dict: {result_dict}")

# ============================================================================
# 4. REVERSING A DICT (SWAP KEYS AND VALUES)
# ============================================================================
print("\n\n4. REVERSING A DICT (SWAP KEYS AND VALUES)")
print("-" * 60)

original = {'a': 1, 'b': 2, 'c': 3}
reversed_dict = {v: k for k, v in original.items()}

print(f"Original: {original}")
print(f"Reversed: {reversed_dict}")

# ============================================================================
# 5. DICT FROM LIST WITH INDEX
# ============================================================================
print("\n\n5. DICT FROM LIST WITH INDEX")
print("-" * 60)

fruits = ['apple', 'banana', 'cherry', 'date']

# Index as key
indexed_dict = {i: fruit for i, fruit in enumerate(fruits)}
print(f"Fruits list: {fruits}")
print(f"With indices: {indexed_dict}")

# Fruit as key
fruit_dict = {fruit: i for i, fruit in enumerate(fruits)}
print(f"Fruit to index: {fruit_dict}")

# ============================================================================
# 6. TRANSFORMING DICT VALUES
# ============================================================================
print("\n\n6. TRANSFORMING DICT VALUES")
print("-" * 60)

original_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Square all values
squared = {k: v ** 2 for k, v in original_dict.items()}
print(f"Original: {original_dict}")
print(f"Squared values: {squared}")

# Convert to string
stringified = {k: str(v) for k, v in original_dict.items()}
print(f"Stringified values: {stringified}")

# ============================================================================
# 7. FILTERING DICT
# ============================================================================
print("\n\n7. FILTERING DICT")
print("-" * 60)

student_ages = {'Alice': 25, 'Bob': 17, 'Charlie': 30, 'Diana': 16}

# Only adults (age >= 18)
adults = {name: age for name, age in student_ages.items() if age >= 18}
print(f"All students: {student_ages}")
print(f"Adults only: {adults}")

# Names starting with 'A' or 'C'
filtered = {name: age for name, age in student_ages.items() if name[0] in ['A', 'C']}
print(f"Names starting with A or C: {filtered}")

# ============================================================================
# 8. NESTED DICT COMPREHENSION
# ============================================================================
print("\n\n8. NESTED DICT COMPREHENSION")
print("-" * 60)

# Create matrix as dict of dicts
matrix_dict = {
    i: {j: i*3 + j for j in range(3)}
    for i in range(3)
}

print("Matrix as nested dict:")
for i, row in matrix_dict.items():
    print(f"  Row {i}: {row}")

# ============================================================================
# 9. DICT COMPREHENSION WITH MULTIPLE CONDITIONS
# ============================================================================
print("\n\n9. DICT COMPREHENSION WITH MULTIPLE CONDITIONS")
print("-" * 60)

# Numbers with multiple conditions
result = {num: num**2 for num in range(20) if num % 2 == 0 if num % 3 == 0}
print(f"Numbers divisible by 2 AND 3: {result}")

# ============================================================================
# 10. MERGING DICTS
# ============================================================================
print("\n\n10. MERGING DICTS")
print("-" * 60)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

# Merge multiple dicts
merged = {k: v for d in [dict1, dict2, dict3] for k, v in d.items()}
print(f"Dict1: {dict1}")
print(f"Dict2: {dict2}")
print(f"Dict3: {dict3}")
print(f"Merged: {merged}")

# ============================================================================
# 11. WORKING WITH STRING VALUES
# ============================================================================
print("\n\n11. WORKING WITH STRING VALUES")
print("-" * 60)

# Convert word length dict
words = ['python', 'java', 'rust', 'go']
word_lengths = {word: len(word) for word in words}
print(f"Words: {words}")
print(f"Word lengths: {word_lengths}")

# Uppercase keys
lowercase_dict = {'name': 'alice', 'city': 'nyc', 'job': 'engineer'}
uppercase_keys = {k.upper(): v for k, v in lowercase_dict.items()}
print(f"\nOriginal: {lowercase_dict}")
print(f"Uppercase keys: {uppercase_keys}")

# ============================================================================
# 12. CONDITIONAL VALUE ASSIGNMENT
# ============================================================================
print("\n\n12. CONDITIONAL VALUE ASSIGNMENT")
print("-" * 60)

# Assign different values based on condition
numbers = range(10)
result_dict = {num: ('even' if num % 2 == 0 else 'odd') for num in numbers}
print(f"Numbers 0-9 with type: {result_dict}")

# Multiply by different factors
factors = {num: (num * 10 if num > 5 else num * 5) for num in range(1, 9)}
print(f"With conditional factors: {factors}")

# ============================================================================
# 13. WORKING WITH DEFAULT VALUES
# ============================================================================
print("\n\n13. WORKING WITH DEFAULT VALUES")
print("-" * 60)

# Use get() for safe access during comprehension
source_dict = {'a': 1, 'b': 2, 'c': 3}
keys_to_check = ['a', 'b', 'd', 'e']

result = {key: source_dict.get(key, 0) for key in keys_to_check}
print(f"Source: {source_dict}")
print(f"Keys to check: {keys_to_check}")
print(f"Result with defaults: {result}")

# ============================================================================
# 14. PRACTICAL EXAMPLES
# ============================================================================
print("\n\n14. PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Word frequency counter (simplified)
text = "apple banana apple cherry banana apple"
words = text.split()
freq = {word: words.count(word) for word in set(words)}
print(f"Text: {text}")
print(f"Word frequency: {freq}")

# Example 2: Temperature conversion
celsius_temps = {'morning': 15, 'noon': 25, 'evening': 20}
fahrenheit_temps = {time: (c * 9/5 + 32) for time, c in celsius_temps.items()}
print(f"\nCelsius: {celsius_temps}")
print(f"Fahrenheit: {fahrenheit_temps}")

# Example 3: Grouping by first letter
words_list = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
grouped = {word[0]: [w for w in words_list if w[0] == word[0]] for word in set(words_list)}
print(f"\nWords: {words_list}")
print(f"Grouped by first letter: {grouped}")

# Example 4: Invert list to dict with indices
items = ['a', 'b', 'c', 'd', 'e']
item_index = {item: idx for idx, item in enumerate(items, 1)}  # Start from 1
print(f"\nItems: {items}")
print(f"Item to index: {item_index}")

# Example 5: Create lookup table
ids = [1, 2, 3, 4, 5]
names = ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve']
lookup = {id_: name for id_, name in zip(ids, names)}
print(f"\nIDs: {ids}")
print(f"Names: {names}")
print(f"Lookup table: {lookup}")

print("\n" + "=" * 60)
print("END OF DICT COMPREHENSIONS TUTORIAL")
print("=" * 60)
