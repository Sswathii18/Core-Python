"""
01_variables_and_types.py
Introduction to Variables and Data Types in Python
"""

print("=" * 60)
print("PYTHON VARIABLES AND DATA TYPES")
print("=" * 60)

# ============================================================================
# 1. VARIABLES AND ASSIGNMENT
# ============================================================================
print("\n1. VARIABLES AND ASSIGNMENT")
print("-" * 60)

# Variables don't need explicit type declaration in Python
name = "Alice"
age = 25
height = 5.7
is_student = True

print(f"Name: {name}")
print(f"Age: {age}")
print(f"Height: {height}")
print(f"Is Student: {is_student}")

# Multiple assignment
x, y, z = 1, 2, 3
print(f"\nMultiple assignment: x={x}, y={y}, z={z}")

# ============================================================================
# 2. DATA TYPES
# ============================================================================
print("\n\n2. DATA TYPES")
print("-" * 60)

# Integer (int)
integer_num = 42
print(f"Integer: {integer_num}, Type: {type(integer_num)}")

# Float
float_num = 3.14159
print(f"Float: {float_num}, Type: {type(float_num)}")

# String (str)
text = "Hello, Python!"
print(f"String: {text}, Type: {type(text)}")

# Boolean (bool)
is_active = True
print(f"Boolean: {is_active}, Type: {type(is_active)}")

# None (NoneType)
empty_value = None
print(f"None: {empty_value}, Type: {type(empty_value)}")

# ============================================================================
# 3. COLLECTIONS
# ============================================================================
print("\n\n3. COLLECTIONS")
print("-" * 60)

# List - ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry", "apple"]
print(f"List: {fruits}")
print(f"Type: {type(fruits)}")
print(f"Length: {len(fruits)}")
print(f"First element: {fruits[0]}")
print(f"Last element: {fruits[-1]}")

# Tuple - ordered, immutable, allows duplicates
coordinates = (10, 20, 30)
print(f"\nTuple: {coordinates}")
print(f"Type: {type(coordinates)}")
print(f"Access element: {coordinates[1]}")

# Dictionary - key-value pairs, mutable, unordered (before Python 3.7)
person = {
    "name": "Bob",
    "age": 30,
    "city": "New York"
}
print(f"\nDictionary: {person}")
print(f"Type: {type(person)}")
print(f"Access value: {person['name']}")
print(f"Keys: {person.keys()}")
print(f"Values: {person.values()}")

# Set - unordered, mutable, no duplicates
unique_numbers = {1, 2, 3, 3, 4}
print(f"\nSet: {unique_numbers}")
print(f"Type: {type(unique_numbers)}")
print(f"Length (note duplicates removed): {len(unique_numbers)}")

# ============================================================================
# 4. TYPE CHECKING AND CONVERSION
# ============================================================================
print("\n\n4. TYPE CHECKING AND CONVERSION")
print("-" * 60)

# Type checking
num = 42
print(f"Is num an integer? {isinstance(num, int)}")
print(f"Is num a string? {isinstance(num, str)}")

# Type conversion
str_num = "123"
int_num = int(str_num)
print(f"\nConverting '123' to integer: {int_num}, Type: {type(int_num)}")

float_from_str = float("3.14")
print(f"Converting '3.14' to float: {float_from_str}, Type: {type(float_from_str)}")

str_from_int = str(100)
print(f"Converting 100 to string: {str_from_int}, Type: {type(str_from_int)}")

# ============================================================================
# 5. STRING OPERATIONS
# ============================================================================
print("\n\n5. STRING OPERATIONS")
print("-" * 60)

text = "Python Programming"

# String indexing
print(f"String: {text}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")

# String slicing
print(f"Slice [0:6]: {text[0:6]}")
print(f"Slice [7:]: {text[7:]}")
print(f"Slice [::2]: {text[::2]}")  # Every 2nd character

# String methods
print(f"Length: {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"Replace 'Python' with 'Java': {text.replace('Python', 'Java')}")
print(f"Split: {text.split()}")

# String formatting
name = "Alice"
age = 25
print(f"\nString formatting:")
print(f"  f-string: {name} is {age} years old")
print(f"  .format(): {} is {} years old".format(name, age))
print(f"  % operator: %s is %d years old" % (name, age))

# ============================================================================
# 6. LIST OPERATIONS
# ============================================================================
print("\n\n6. LIST OPERATIONS")
print("-" * 60)

numbers = [1, 2, 3, 4, 5]
print(f"Original list: {numbers}")

# List methods
numbers.append(6)
print(f"After append(6): {numbers}")

numbers.extend([7, 8])
print(f"After extend([7, 8]): {numbers}")

numbers.remove(3)
print(f"After remove(3): {numbers}")

popped = numbers.pop()
print(f"Popped element: {popped}, List: {numbers}")

# ============================================================================
# 7. DICTIONARY OPERATIONS
# ============================================================================
print("\n\n7. DICTIONARY OPERATIONS")
print("-" * 60)

student = {
    "name": "Charlie",
    "grade": "A",
    "gpa": 3.9
}

print(f"Original dictionary: {student}")
print(f"Get name: {student.get('name')}")
print(f"Get age (with default): {student.get('age', 'Not found')}")

# Add new key-value
student["age"] = 20
print(f"After adding age: {student}")

# Update values
student.update({"grade": "A+", "gpa": 4.0})
print(f"After update: {student}")

# Remove item
removed_value = student.pop("age")
print(f"Removed age: {removed_value}, Dictionary: {student}")

# ============================================================================
# 8. TYPE AND MEMORY INFO
# ============================================================================
print("\n\n8. TYPE AND MEMORY INFO")
print("-" * 60)

variables = [42, 3.14, "text", True, [1, 2], {"a": 1}]
for var in variables:
    print(f"Value: {var!r:20} | Type: {type(var).__name__:10} | Size: {len(str(var))}")

print("\n" + "=" * 60)
print("END OF VARIABLES AND DATA TYPES TUTORIAL")
print("=" * 60)
