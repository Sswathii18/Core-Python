"""
01_basic_type_hints.py
Introduction to Type Hints in Python
"""

print("=" * 60)
print("PYTHON TYPE HINTS - BASICS")
print("=" * 60)

# ============================================================================
# 1. FUNCTION PARAMETER HINTS
# ============================================================================
print("\n1. FUNCTION PARAMETER HINTS")
print("-" * 60)

def greet(name: str) -> str:
    """Greet a person with their name."""
    return f"Hello, {name}!"

print("Function with type hints:")
print("  def greet(name: str) -> str:")
result = greet("Alice")
print(f"  greet('Alice') = {result}")

# ============================================================================
# 2. MULTIPLE PARAMETERS WITH HINTS
# ============================================================================
print("\n\n2. MULTIPLE PARAMETERS WITH HINTS")
print("-" * 60)

def add(a: int, b: int) -> int:
    """Add two integers."""
    return a + b

def divide(a: float, b: float) -> float:
    """Divide two floating-point numbers."""
    return a / b

print("Multiple parameter hints:")
print(f"  add(5, 3) = {add(5, 3)}")
print(f"  divide(10.0, 3.0) = {divide(10.0, 3.0):.2f}")

# ============================================================================
# 3. VARIABLE TYPE HINTS
# ============================================================================
print("\n\n3. VARIABLE TYPE HINTS")
print("-" * 60)

# Basic variable types
name: str = "Alice"
age: int = 25
height: float = 5.7
is_student: bool = True

print("Variable type hints:")
print(f"  name: str = {name}")
print(f"  age: int = {age}")
print(f"  height: float = {height}")
print(f"  is_student: bool = {is_student}")

# ============================================================================
# 4. COLLECTION TYPE HINTS
# ============================================================================
print("\n\n4. COLLECTION TYPE HINTS")
print("-" * 60)

from typing import List, Dict, Set, Tuple

# List of integers
numbers: List[int] = [1, 2, 3, 4, 5]
print(f"List[int]: {numbers}")

# Dictionary with string keys and int values
ages: Dict[str, int] = {"Alice": 30, "Bob": 25}
print(f"Dict[str, int]: {ages}")

# Set of strings
tags: Set[str] = {"python", "coding", "tutorial"}
print(f"Set[str]: {tags}")

# Tuple with specific types
coordinates: Tuple[int, int] = (10, 20)
print(f"Tuple[int, int]: {coordinates}")

# ============================================================================
# 5. OPTIONAL TYPES
# ============================================================================
print("\n\n5. OPTIONAL TYPES")
print("-" * 60)

from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    """Find user by ID, return name or None."""
    users = {1: "Alice", 2: "Bob", 3: "Charlie"}
    return users.get(user_id)

print("Optional type hints:")
print(f"  find_user(1) = {find_user(1)}")
print(f"  find_user(999) = {find_user(999)}")

def greet_user(name: Optional[str] = None) -> str:
    """Greet user if name is provided."""
    if name is None:
        return "Hello, stranger!"
    return f"Hello, {name}!"

print(f"  greet_user() = {greet_user()}")
print(f"  greet_user('Alice') = {greet_user('Alice')}")

# ============================================================================
# 6. UNION TYPES
# ============================================================================
print("\n\n6. UNION TYPES")
print("-" * 60)

from typing import Union

def process_value(value: Union[int, str]) -> str:
    """Process value that can be int or str."""
    return f"Processed: {value}"

print("Union type hints:")
print(f"  process_value(42) = {process_value(42)}")
print(f"  process_value('text') = {process_value('text')}")

# ============================================================================
# 7. DEFAULT VALUES WITH TYPE HINTS
# ============================================================================
print("\n\n7. DEFAULT VALUES WITH TYPE HINTS")
print("-" * 60)

def calculate_total(price: float, tax: float = 0.1) -> float:
    """Calculate total with optional tax."""
    return price * (1 + tax)

print("Default values with type hints:")
print(f"  calculate_total(100) = {calculate_total(100)}")
print(f"  calculate_total(100, 0.2) = {calculate_total(100, 0.2)}")

# ============================================================================
# 8. FUNCTION WITH MULTIPLE RETURN TYPES
# ============================================================================
print("\n\n8. FUNCTION WITH MULTIPLE RETURN TYPES")
print("-" * 60)

def get_user_info(user_id: int) -> Union[Dict[str, str], None]:
    """Get user info or return None if not found."""
    users = {
        1: {"name": "Alice", "role": "admin"},
        2: {"name": "Bob", "role": "user"}
    }
    return users.get(user_id)

print("Multiple return types:")
print(f"  get_user_info(1) = {get_user_info(1)}")
print(f"  get_user_info(999) = {get_user_info(999)}")

# ============================================================================
# 9. LIST AND DICT WITH HINTS
# ============================================================================
print("\n\n9. LIST AND DICT WITH HINTS")
print("-" * 60)

def process_students(students: List[Dict[str, Union[str, int]]]) -> List[str]:
    """Process list of student dictionaries."""
    return [f"{s['name']} ({s['age']})" for s in students]

students_data: List[Dict[str, Union[str, int]]] = [
    {"name": "Alice", "age": 20},
    {"name": "Bob", "age": 21},
    {"name": "Charlie", "age": 20}
]

print("Complex list and dict hints:")
print(f"  {process_students(students_data)}")

# ============================================================================
# 10. TUPLE RETURN VALUES
# ============================================================================
print("\n\n10. TUPLE RETURN VALUES")
print("-" * 60)

def get_min_max(numbers: List[int]) -> Tuple[int, int]:
    """Return min and max of numbers."""
    return min(numbers), max(numbers)

print("Tuple return types:")
nums = [5, 2, 8, 1, 9]
min_val, max_val = get_min_max(nums)
print(f"  get_min_max({nums}) = ({min_val}, {max_val})")

# ============================================================================
# 11. NONE TYPE
# ============================================================================
print("\n\n11. NONE TYPE")
print("-" * 60)

def print_message(message: str) -> None:
    """Print message (returns None)."""
    print(f"  Message: {message}")

print("Functions that return None:")
result = print_message("Hello")
print(f"  Return value: {result}")

# ============================================================================
# 12. TYPE ALIASES
# ============================================================================
print("\n\n12. TYPE ALIASES")
print("-" * 60)

# Create type aliases for readability
UserId = int
UserName = str
UserData = Dict[str, Union[str, int]]

def get_user_by_id(user_id: UserId) -> Optional[UserName]:
    """Get username by user ID."""
    users: Dict[UserId, UserName] = {
        1: "Alice",
        2: "Bob",
        3: "Charlie"
    }
    return users.get(user_id)

print("Type aliases for readability:")
print(f"  get_user_by_id(1) = {get_user_by_id(1)}")
print(f"  get_user_by_id(999) = {get_user_by_id(999)}")

# ============================================================================
# 13. PRACTICAL EXAMPLES
# ============================================================================
print("\n\n13. PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Validate email
def is_valid_email(email: str) -> bool:
    """Validate email format."""
    return "@" in email and "." in email

print("Email validation:")
print(f"  is_valid_email('user@example.com') = {is_valid_email('user@example.com')}")
print(f"  is_valid_email('invalid-email') = {is_valid_email('invalid-email')}")

# Example 2: Calculate statistics
def calculate_stats(numbers: List[float]) -> Dict[str, float]:
    """Calculate mean, min, max."""
    if not numbers:
        return {}
    
    return {
        "mean": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }

print("\nCalculate statistics:")
data: List[float] = [10, 20, 30, 40, 50]
stats = calculate_stats(data)
print(f"  Data: {data}")
print(f"  Stats: {stats}")

# Example 3: Filter and transform
def filter_and_transform(
    items: List[int],
    min_value: int = 0,
    transform_func: Optional[callable] = None
) -> List[Union[int, float]]:
    """Filter items and optionally transform them."""
    filtered = [x for x in items if x >= min_value]
    if transform_func:
        return [transform_func(x) for x in filtered]
    return filtered

print("\nFilter and transform:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = filter_and_transform(numbers, min_value=5, transform_func=lambda x: x ** 2)
print(f"  Numbers >= 5 squared: {result}")

print("\n" + "=" * 60)
print("END OF BASIC TYPE HINTS TUTORIAL")
print("=" * 60)
