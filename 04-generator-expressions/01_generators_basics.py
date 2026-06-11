"""
01_generators_basics.py
Understanding Generators in Python
"""

print("=" * 60)
print("PYTHON GENERATORS - BASICS")
print("=" * 60)

# ============================================================================
# 1. SIMPLE GENERATOR FUNCTION
# ============================================================================
print("\n1. SIMPLE GENERATOR FUNCTION")
print("-" * 60)

def count_up_to(n):
    """Generator that yields numbers from 1 to n."""
    i = 1
    while i <= n:
        print(f"  Generating {i}")
        yield i
        i += 1

print("Creating generator:")
gen = count_up_to(3)
print(f"Generator object: {gen}")

print("\nIterating through generator:")
for num in gen:
    print(f"  Got: {num}")

# ============================================================================
# 2. GENERATOR vs LIST
# ============================================================================
print("\n\n2. GENERATOR vs LIST")
print("-" * 60)

# List approach - loads all data into memory
print("List approach:")
numbers_list = [x ** 2 for x in range(5)]
print(f"  List: {numbers_list}")

# Generator approach - lazy evaluation
print("\nGenerator approach:")
def numbers_generator():
    for x in range(5):
        yield x ** 2

gen = numbers_generator()
print(f"  Generator: {gen}")
print(f"  Consuming generator:")
for num in gen:
    print(f"    {num}")

# ============================================================================
# 3. MEMORY EFFICIENCY
# ============================================================================
print("\n\n3. MEMORY EFFICIENCY")
print("-" * 60)

import sys

# Large list
large_list = [x ** 2 for x in range(1000)]
print(f"List size (1000 elements): {sys.getsizeof(large_list)} bytes")

# Generator
def large_generator():
    for x in range(1000):
        yield x ** 2

gen = large_generator()
print(f"Generator size: {sys.getsizeof(gen)} bytes")

# ============================================================================
# 4. YIELD KEYWORD
# ============================================================================
print("\n\n4. YIELD KEYWORD")
print("-" * 60)

def fibonacci(n):
    """Generate Fibonacci sequence with n terms."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("Fibonacci sequence (first 7 numbers):")
for num in fibonacci(7):
    print(f"  {num}", end=" ")
print()

# ============================================================================
# 5. GENERATOR WITH EARLY EXIT
# ============================================================================
print("\n\n5. GENERATOR WITH EARLY EXIT")
print("-" * 60)

def count_to_ten():
    """Count from 1 to 10."""
    for i in range(1, 11):
        print(f"  Yielding {i}")
        yield i

print("Early exit from generator (break at 5):")
for num in count_to_ten():
    print(f"  Got: {num}")
    if num == 5:
        break

# ============================================================================
# 6. GENERATOR EXPRESSIONS
# ============================================================================
print("\n\n6. GENERATOR EXPRESSIONS")
print("-" * 60)

# List comprehension
squares_list = [x ** 2 for x in range(5)]
print(f"List comprehension: {squares_list}")

# Generator expression (same syntax with parentheses)
squares_gen = (x ** 2 for x in range(5))
print(f"Generator expression: {squares_gen}")
print(f"Consuming generator expression:")
for num in squares_gen:
    print(f"  {num}")

# ============================================================================
# 7. NEXT() FUNCTION
# ============================================================================
print("\n\n7. NEXT() FUNCTION")
print("-" * 60)

def simple_count():
    yield 1
    yield 2
    yield 3

gen = simple_count()
print(f"First call to next(): {next(gen)}")
print(f"Second call to next(): {next(gen)}")
print(f"Third call to next(): {next(gen)}")

try:
    print(f"Fourth call to next(): {next(gen)}")
except StopIteration:
    print("  StopIteration raised - no more values")

# ============================================================================
# 8. GENERATOR WITH CONDITION
# ============================================================================
print("\n\n8. GENERATOR WITH CONDITION")
print("-" * 60)

def even_numbers(n):
    """Generate even numbers up to n."""
    for i in range(n):
        if i % 2 == 0:
            yield i

print("Even numbers from 0-10:")
for num in even_numbers(11):
    print(f"  {num}", end=" ")
print()

# ============================================================================
# 9. GENERATOR CHAINING
# ============================================================================
print("\n\n9. GENERATOR CHAINING")
print("-" * 60)

def numbers():
    """Generate numbers 1-5."""
    for i in range(1, 6):
        yield i

def squares(nums):
    """Generate squares of numbers."""
    for num in nums:
        yield num ** 2

def filter_large(nums):
    """Filter numbers > 10."""
    for num in nums:
        if num > 10:
            yield num

print("Chaining generators (numbers -> squares -> filter):")
result = filter_large(squares(numbers()))
for num in result:
    print(f"  {num}")

# ============================================================================
# 10. READING FILES WITH GENERATOR
# ============================================================================
print("\n\n10. READING FILES WITH GENERATOR")
print("-" * 60)

def read_file_lines(filename):
    """Read file line by line without loading all into memory."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"  File '{filename}' not found")

# Example (file doesn't exist, but shows the pattern)
print("Generator for reading files line by line:")
print(f"  Function: read_file_lines(filename)")
print(f"  Usage: for line in read_file_lines('file.txt'):")

# ============================================================================
# 11. INFINITE GENERATOR
# ============================================================================
print("\n\n11. INFINITE GENERATOR")
print("-" * 60)

def infinite_counter(start=0):
    """Generate infinite sequence of numbers."""
    n = start
    while True:
        yield n
        n += 1

print("Using infinite generator (first 5 numbers):")
counter = infinite_counter(100)
for _ in range(5):
    print(f"  {next(counter)}", end=" ")
print()

# ============================================================================
# 12. GENERATOR WITH SEND()
# ============================================================================
print("\n\n12. GENERATOR WITH SEND()")
print("-" * 60)

def echo():
    """Generator that can receive values."""
    value = None
    while True:
        value = yield value
        if value is not None:
            value = value * 2

print("Using send() to communicate with generator:")
gen = echo()
print(f"  Initial: {next(gen)}")
print(f"  After send(5): {gen.send(5)}")
print(f"  After send(10): {gen.send(10)}")
print(f"  After send(3): {gen.send(3)}")

# ============================================================================
# 13. PRACTICAL EXAMPLES
# ============================================================================
print("\n\n13. PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Sensor data stream
def sensor_readings(count):
    """Simulate sensor readings."""
    for i in range(count):
        yield 20 + i * 0.5  # Temperature increasing

print("Sensor readings (first 5):")
for reading in sensor_readings(5):
    print(f"  {reading:.1f}°C")

# Example 2: Batch processing
def batch_items(items, batch_size):
    """Yield items in batches."""
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]

data = range(1, 11)
print("\nBatch processing (batch size 3):")
for batch in batch_items(list(data), 3):
    print(f"  {batch}")

# Example 3: Unique items preserving order
def unique_items(items):
    """Yield unique items preserving order."""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

print("\nUnique items (from [1, 2, 2, 3, 3, 3, 4]):")
data = [1, 2, 2, 3, 3, 3, 4]
for item in unique_items(data):
    print(f"  {item}", end=" ")
print()

print("\n" + "=" * 60)
print("END OF GENERATORS BASICS TUTORIAL")
print("=" * 60)
