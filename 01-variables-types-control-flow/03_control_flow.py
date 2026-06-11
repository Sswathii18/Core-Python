"""
03_control_flow.py
Understanding Control Flow in Python
"""

print("=" * 60)
print("PYTHON CONTROL FLOW")
print("=" * 60)

# ============================================================================
# 1. IF STATEMENTS
# ============================================================================
print("\n1. IF STATEMENTS")
print("-" * 60)

age = 20
print(f"Age: {age}")

if age >= 18:
    print("You are an adult!")

# ============================================================================
# 2. IF-ELSE STATEMENTS
# ============================================================================
print("\n\n2. IF-ELSE STATEMENTS")
print("-" * 60)

score = 45
print(f"Score: {score}")

if score >= 50:
    print("PASS")
else:
    print("FAIL")

# ============================================================================
# 3. IF-ELIF-ELSE STATEMENTS
# ============================================================================
print("\n\n3. IF-ELIF-ELSE STATEMENTS")
print("-" * 60)

grade_score = 85
print(f"Score: {grade_score}")

if grade_score >= 90:
    grade = "A"
elif grade_score >= 80:
    grade = "B"
elif grade_score >= 70:
    grade = "C"
elif grade_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")

# ============================================================================
# 4. NESTED IF STATEMENTS
# ============================================================================
print("\n\n4. NESTED IF STATEMENTS")
print("-" * 60)

age = 25
has_license = True

print(f"Age: {age}, Has License: {has_license}")

if age >= 18:
    print("You are eligible to drive")
    if has_license:
        print("You can drive!")
    else:
        print("You need to get a license first")
else:
    print("You are too young to drive")

# ============================================================================
# 5. TERNARY OPERATOR (Conditional Expression)
# ============================================================================
print("\n\n5. TERNARY OPERATOR (Conditional Expression)")
print("-" * 60)

age = 20
status = "Adult" if age >= 18 else "Minor"
print(f"Age {age} -> {status}")

# More complex example
num = 10
result = "Positive" if num > 0 else "Negative" if num < 0 else "Zero"
print(f"Number {num} -> {result}")

# ============================================================================
# 6. FOR LOOPS
# ============================================================================
print("\n\n6. FOR LOOPS")
print("-" * 60)

# Loop through a range
print("Counting from 0 to 4:")
for i in range(5):
    print(f"  {i}")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
print("\nLooping through list:")
for fruit in fruits:
    print(f"  - {fruit}")

# Loop with index
print("\nLooping with index:")
for index, fruit in enumerate(fruits):
    print(f"  {index}: {fruit}")

# Nested loops
print("\nMultiplication table (2x3):")
for i in range(1, 3):
    for j in range(1, 4):
        print(f"  {i} x {j} = {i*j}")

# ============================================================================
# 7. WHILE LOOPS
# ============================================================================
print("\n\n7. WHILE LOOPS")
print("-" * 60)

count = 0
print("Counting with while loop:")
while count < 5:
    print(f"  Count: {count}")
    count += 1

# While with condition
num = 100
print("\nDividing by 2 until less than 10:")
while num >= 10:
    print(f"  {num}")
    num = num // 2

# ============================================================================
# 8. BREAK STATEMENT
# ============================================================================
print("\n\n8. BREAK STATEMENT")
print("-" * 60)

print("Finding first even number:")
for i in range(1, 10):
    if i % 2 == 0:
        print(f"  Found: {i}")
        break

# ============================================================================
# 9. CONTINUE STATEMENT
# ============================================================================
print("\n\n9. CONTINUE STATEMENT")
print("-" * 60)

print("Printing odd numbers from 1 to 10:")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(f"  {i}")

# ============================================================================
# 10. ELSE WITH LOOPS
# ============================================================================
print("\n\n10. ELSE WITH LOOPS")
print("-" * 60)

# For-else
print("For-else (no break):")
for i in range(3):
    print(f"  Iteration {i}")
else:
    print("  Loop completed normally")

print("\nFor-else (with break):")
for i in range(3):
    if i == 1:
        print(f"  Breaking at {i}")
        break
    print(f"  Iteration {i}")
else:
    print("  This won't print because of break")

# ============================================================================
# 11. PASS STATEMENT
# ============================================================================
print("\n\n11. PASS STATEMENT")
print("-" * 60)

for i in range(3):
    if i == 1:
        pass  # Placeholder, do nothing
    else:
        print(f"  Number: {i}")

# ============================================================================
# 12. PRACTICAL EXAMPLES
# ============================================================================
print("\n\n12. PRACTICAL EXAMPLES")
print("-" * 60)

# Example 1: Validate user input
print("Example 1: Validate password")
password = "Pass123"
if len(password) >= 8:
    if any(char.isdigit() for char in password):
        if any(char.isupper() for char in password):
            print(f"  Password '{password}' is strong!")
        else:
            print("  Password needs uppercase letters")
    else:
        print("  Password needs digits")
else:
    print("  Password too short")

# Example 2: Find sum of numbers
print("\nExample 2: Sum numbers until negative")
total = 0
numbers = [5, 10, 3, -1, 8, 2]
for num in numbers:
    if num < 0:
        break
    total += num
print(f"  Sum: {total}")

# Example 3: Check if number is prime
print("\nExample 3: Check if numbers are prime")
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

for num in [2, 3, 4, 5, 10, 11]:
    print(f"  {num}: {'Prime' if is_prime(num) else 'Not Prime'}")

print("\n" + "=" * 60)
print("END OF CONTROL FLOW TUTORIAL")
print("=" * 60)
