"""
02_operators.py
Understanding Python Operators
"""

print("=" * 60)
print("PYTHON OPERATORS")
print("=" * 60)

# ============================================================================
# 1. ARITHMETIC OPERATORS
# ============================================================================
print("\n1. ARITHMETIC OPERATORS")
print("-" * 60)

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")
print(f"Floor Division (a // b): {a // b}")
print(f"Modulo (a % b): {a % b}")
print(f"Exponentiation (a ** b): {a ** b}")

# ============================================================================
# 2. COMPARISON OPERATORS
# ============================================================================
print("\n\n2. COMPARISON OPERATORS")
print("-" * 60)

x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"x == y (equal): {x == y}")
print(f"x != y (not equal): {x != y}")
print(f"x < y (less than): {x < y}")
print(f"x > y (greater than): {x > y}")
print(f"x <= y (less than or equal): {x <= y}")
print(f"x >= y (greater than or equal): {x >= y}")

# ============================================================================
# 3. LOGICAL OPERATORS
# ============================================================================
print("\n\n3. LOGICAL OPERATORS")
print("-" * 60)

condition1 = True
condition2 = False

print(f"condition1 = {condition1}, condition2 = {condition2}")
print(f"condition1 and condition2: {condition1 and condition2}")
print(f"condition1 or condition2: {condition1 or condition2}")
print(f"not condition1: {not condition1}")

# Practical example with conditions
age = 25
income = 50000

print(f"\nAge: {age}, Income: {income}")
print(f"Can apply for loan (age >= 18 and income >= 30000): {age >= 18 and income >= 30000}")
print(f"Is student or unemployed (is_student or unemployed): False or True = {False or True}")

# ============================================================================
# 4. ASSIGNMENT OPERATORS
# ============================================================================
print("\n\n4. ASSIGNMENT OPERATORS")
print("-" * 60)

num = 10
print(f"Initial value: num = {num}")

num += 5
print(f"After += 5: num = {num}")

num -= 3
print(f"After -= 3: num = {num}")

num *= 2
print(f"After *= 2: num = {num}")

num /= 4
print(f"After /= 4: num = {num}")

num //= 2
print(f"After //= 2: num = {num}")

num **= 2
print(f"After **= 2: num = {num}")

num %= 5
print(f"After %= 5: num = {num}")

# ============================================================================
# 5. MEMBERSHIP OPERATORS
# ============================================================================
print("\n\n5. MEMBERSHIP OPERATORS")
print("-" * 60)

fruits = ["apple", "banana", "cherry"]
print(f"List: {fruits}")
print(f"'apple' in fruits: {'apple' in fruits}")
print(f"'grape' in fruits: {'grape' in fruits}")
print(f"'apple' not in fruits: {'apple' not in fruits}")

# ============================================================================
# 6. IDENTITY OPERATORS
# ============================================================================
print("\n\n6. IDENTITY OPERATORS")
print("-" * 60)

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(f"a = {a}")
print(f"b = {b}")
print(f"c = a")
print(f"a == b (value equal): {a == b}")
print(f"a is b (same object): {a is b}")
print(f"a is c (same object): {a is c}")

# ============================================================================
# 7. BITWISE OPERATORS
# ============================================================================
print("\n\n7. BITWISE OPERATORS")
print("-" * 60)

x = 5      # Binary: 0101
y = 3      # Binary: 0011

print(f"x = {x} (Binary: {bin(x)})")
print(f"y = {y} (Binary: {bin(y)})")
print(f"x & y (AND): {x & y} (Binary: {bin(x & y)})")
print(f"x | y (OR): {x | y} (Binary: {bin(x | y)})")
print(f"x ^ y (XOR): {x ^ y} (Binary: {bin(x ^ y)})")
print(f"~x (NOT): {~x} (Binary: {bin(~x & 0xFF)})")
print(f"x << 1 (Left shift): {x << 1} (Binary: {bin(x << 1)})")
print(f"x >> 1 (Right shift): {x >> 1} (Binary: {bin(x >> 1)})")

# ============================================================================
# 8. OPERATOR PRECEDENCE
# ============================================================================
print("\n\n8. OPERATOR PRECEDENCE")
print("-" * 60)

# Precedence (highest to lowest):
# 1. ** (Exponentiation)
# 2. *, /, //, % (Multiplication, Division, Floor Division, Modulo)
# 3. +, - (Addition, Subtraction)
# 4. <, >, <=, >=, ==, != (Comparisons)
# 5. and, or, not (Logical)

result1 = 2 + 3 * 4
result2 = (2 + 3) * 4

print(f"2 + 3 * 4 = {result1}  (Multiplication first)")
print(f"(2 + 3) * 4 = {result2}  (Parentheses first)")

result3 = 10 - 5 - 2
result4 = 10 - (5 - 2)

print(f"10 - 5 - 2 = {result3}  (Left to right)")
print(f"10 - (5 - 2) = {result4}  (Parentheses first)")

# ============================================================================
# 9. CHAINING COMPARISONS
# ============================================================================
print("\n\n9. CHAINING COMPARISONS")
print("-" * 60)

age = 25

# Traditional way
if age >= 18 and age < 65:
    print(f"Age {age}: Adult (traditional)")

# Chained comparison
if 18 <= age < 65:
    print(f"Age {age}: Adult (chained)")

# More complex
score = 75
if 0 <= score <= 100:
    print(f"Score {score}: Valid")

print("\n" + "=" * 60)
print("END OF OPERATORS TUTORIAL")
print("=" * 60)
