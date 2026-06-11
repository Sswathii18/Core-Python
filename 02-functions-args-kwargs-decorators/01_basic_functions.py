"""
01_basic_functions.py
Introduction to Functions in Python
"""

print("=" * 60)
print("PYTHON FUNCTIONS - BASICS")
print("=" * 60)

# ============================================================================
# 1. SIMPLE FUNCTION
# ============================================================================
print("\n1. SIMPLE FUNCTION")
print("-" * 60)

def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")

greet()

# ============================================================================
# 2. FUNCTION WITH PARAMETERS
# ============================================================================
print("\n\n2. FUNCTION WITH PARAMETERS")
print("-" * 60)

def greet_person(name):
    """Function that takes a name parameter."""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# ============================================================================
# 3. FUNCTION WITH MULTIPLE PARAMETERS
# ============================================================================
print("\n\n3. FUNCTION WITH MULTIPLE PARAMETERS")
print("-" * 60)

def add(a, b):
    """Function that adds two numbers."""
    result = a + b
    return result

sum_result = add(5, 3)
print(f"add(5, 3) = {sum_result}")

# ============================================================================
# 4. FUNCTION WITH RETURN VALUE
# ============================================================================
print("\n\n4. FUNCTION WITH RETURN VALUE")
print("-" * 60)

def multiply(x, y):
    """Function that returns the product of two numbers."""
    return x * y

product = multiply(4, 7)
print(f"multiply(4, 7) = {product}")

# Multiple return values
def get_coordinates():
    """Function that returns multiple values."""
    x = 10
    y = 20
    return x, y

coord_x, coord_y = get_coordinates()
print(f"Coordinates: x={coord_x}, y={coord_y}")

# ============================================================================
# 5. DEFAULT PARAMETERS
# ============================================================================
print("\n\n5. DEFAULT PARAMETERS")
print("-" * 60)

def greet_with_title(name, title="Mr/Ms"):
    """Function with default parameter."""
    print(f"Hello, {title} {name}!")

greet_with_title("Smith")
greet_with_title("Johnson", "Dr")

# ============================================================================
# 6. KEYWORD ARGUMENTS
# ============================================================================
print("\n\n6. KEYWORD ARGUMENTS")
print("-" * 60)

def describe_person(name, age, city):
    """Function with keyword arguments."""
    print(f"Name: {name}, Age: {age}, City: {city}")

# Positional arguments
describe_person("Alice", 30, "New York")

# Keyword arguments
describe_person(city="Los Angeles", name="Bob", age=25)

# Mix of both
describe_person("Charlie", age=35, city="Chicago")

# ============================================================================
# 7. DOCSTRINGS AND HELP
# ============================================================================
print("\n\n7. DOCSTRINGS AND HELP")
print("-" * 60)

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Parameters:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area of the rectangle
    """
    return length * width

print("Function docstring:")
print(calculate_area.__doc__)

# ============================================================================
# 8. VARIABLE SCOPE
# ============================================================================
print("\n\n8. VARIABLE SCOPE")
print("-" * 60)

global_var = "I'm global"

def demonstrate_scope():
    """Demonstrate variable scope."""
    local_var = "I'm local"
    print(f"  Inside function - local_var: {local_var}")
    print(f"  Inside function - global_var: {global_var}")

print("Outside function:")
print(f"  global_var: {global_var}")

demonstrate_scope()

# This will cause an error if uncommented:
# print(local_var)  # NameError: local_var is not defined

# ============================================================================
# 9. USING GLOBAL AND NONLOCAL
# ============================================================================
print("\n\n9. USING GLOBAL AND NONLOCAL")
print("-" * 60)

counter = 0

def increment_counter():
    """Modify global variable."""
    global counter
    counter += 1
    print(f"  Counter: {counter}")

print("Incrementing counter:")
increment_counter()
increment_counter()
increment_counter()

# ============================================================================
# 10. FUNCTION THAT CALLS ANOTHER FUNCTION
# ============================================================================
print("\n\n10. FUNCTION THAT CALLS ANOTHER FUNCTION")
print("-" * 60)

def square(x):
    """Return the square of a number."""
    return x ** 2

def sum_of_squares(a, b):
    """Return the sum of squares of two numbers."""
    return square(a) + square(b)

result = sum_of_squares(3, 4)
print(f"sum_of_squares(3, 4) = {result}")

# ============================================================================
# 11. RECURSION
# ============================================================================
print("\n\n11. RECURSION")
print("-" * 60)

def factorial(n):
    """Calculate factorial using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")

def fibonacci(n):
    """Generate fibonacci number at position n."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(f"fibonacci(7) = {fibonacci(7)}")

# ============================================================================
# 12. LAMBDA FUNCTIONS
# ============================================================================
print("\n\n12. LAMBDA FUNCTIONS")
print("-" * 60)

# Simple lambda
square_lambda = lambda x: x ** 2
print(f"lambda x: x**2 applied to 5 = {square_lambda(5)}")

# Lambda with multiple arguments
add_lambda = lambda x, y: x + y
print(f"lambda x, y: x+y with (3, 7) = {add_lambda(3, 7)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squares of {numbers}: {squared}")

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers from {numbers}: {evens}")

# ============================================================================
# 13. PRACTICAL EXAMPLES
# ============================================================================
print("\n\n13. PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Validate email
def is_valid_email(email):
    """Simple email validation."""
    return "@" in email and "." in email

print("Email validation:")
print(f"  user@example.com: {is_valid_email('user@example.com')}")
print(f"  invalid-email: {is_valid_email('invalid-email')}")

# Example 2: Password strength checker
def check_password_strength(password):
    """Check password strength."""
    strength = 0
    
    if len(password) >= 8:
        strength += 1
    if any(char.isdigit() for char in password):
        strength += 1
    if any(char.isupper() for char in password):
        strength += 1
    if any(char.islower() for char in password):
        strength += 1
    
    if strength <= 1:
        return "Weak"
    elif strength <= 2:
        return "Fair"
    elif strength <= 3:
        return "Good"
    else:
        return "Strong"

print("\nPassword strength:")
print(f"  '123': {check_password_strength('123')}")
print(f"  'Password': {check_password_strength('Password')}")
print(f"  'Pass123!': {check_password_strength('Pass123!')}")

print("\n" + "=" * 60)
print("END OF BASIC FUNCTIONS TUTORIAL")
print("=" * 60)
