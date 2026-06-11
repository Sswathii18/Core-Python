"""
02_args_kwargs.py
Understanding *args and **kwargs in Python
"""

print("=" * 60)
print("PYTHON *args AND **kwargs")
print("=" * 60)

# ============================================================================
# 1. *args (Variable Positional Arguments)
# ============================================================================
print("\n1. *args (VARIABLE POSITIONAL ARGUMENTS)")
print("-" * 60)

def print_args(*args):
    """Function that accepts any number of positional arguments."""
    print(f"  Type of args: {type(args)}")
    print(f"  Number of arguments: {len(args)}")
    for i, arg in enumerate(args):
        print(f"    arg[{i}]: {arg}")

print("Calling print_args(1, 2, 3):")
print_args(1, 2, 3)

print("\nCalling print_args('a', 'b', 'c', 'd'):")
print_args('a', 'b', 'c', 'd')

# ============================================================================
# 2. FUNCTION WITH *args - SUM ALL NUMBERS
# ============================================================================
print("\n\n2. FUNCTION WITH *args - SUM ALL NUMBERS")
print("-" * 60)

def sum_all(*numbers):
    """Sum all numbers passed as arguments."""
    total = 0
    for num in numbers:
        total += num
    return total

print(f"sum_all(1, 2, 3) = {sum_all(1, 2, 3)}")
print(f"sum_all(10, 20, 30, 40, 50) = {sum_all(10, 20, 30, 40, 50)}")
print(f"sum_all(5) = {sum_all(5)}")

# ============================================================================
# 3. **kwargs (VARIABLE KEYWORD ARGUMENTS)
# ============================================================================
print("\n\n3. **kwargs (VARIABLE KEYWORD ARGUMENTS)")
print("-" * 60)

def print_kwargs(**kwargs):
    """Function that accepts any number of keyword arguments."""
    print(f"  Type of kwargs: {type(kwargs)}")
    print(f"  Number of arguments: {len(kwargs)}")
    for key, value in kwargs.items():
        print(f"    {key}: {value}")

print("Calling print_kwargs(name='Alice', age=30, city='NYC'):")
print_kwargs(name='Alice', age=30, city='NYC')

print("\nCalling print_kwargs(color='red', size='large'):")
print_kwargs(color='red', size='large')

# ============================================================================
# 4. COMBINING *args AND **kwargs
# ============================================================================
print("\n\n4. COMBINING *args AND **kwargs")
print("-" * 60)

def function_with_both(name, *args, **kwargs):
    """Function with regular parameter, *args, and **kwargs."""
    print(f"  name: {name}")
    print(f"  args: {args}")
    print(f"  kwargs: {kwargs}")

print("Calling function_with_both('Alice', 1, 2, 3, color='red', size='large'):")
function_with_both('Alice', 1, 2, 3, color='red', size='large')

# ============================================================================
# 5. UNPACKING WITH *args
# ============================================================================
print("\n\n5. UNPACKING WITH *args")
print("-" * 60)

def print_numbers(a, b, c):
    """Function that takes three parameters."""
    print(f"  a={a}, b={b}, c={c}")

numbers = [10, 20, 30]
print("Using unpacking with *:")
print_numbers(*numbers)

# ============================================================================
# 6. UNPACKING WITH **kwargs
# ============================================================================
print("\n\n6. UNPACKING WITH **kwargs")
print("-" * 60)

def print_person(name, age, city):
    """Function with three parameters."""
    print(f"  Name: {name}, Age: {age}, City: {city}")

person_info = {'name': 'Bob', 'age': 25, 'city': 'LA'}
print("Using unpacking with **:")
print_person(**person_info)

# ============================================================================
# 7. PRACTICAL EXAMPLE: PRINT TABLE
# ============================================================================
print("\n\n7. PRACTICAL EXAMPLE: PRINT TABLE")
print("-" * 60)

def print_table(**kwargs):
    """Print table with given headers and data."""
    # Print headers
    headers = kwargs.keys()
    print("  | ".join(headers))
    print("-" * 50)
    
    # Print values
    values = kwargs.values()
    print("  | ".join(str(v) for v in values))

print("Print table:")
print_table(Name='Alice', Age='30', City='New York', Job='Engineer')

# ============================================================================
# 8. PRACTICAL EXAMPLE: FLEXIBLE FUNCTION
# ============================================================================
print("\n\n8. PRACTICAL EXAMPLE: FLEXIBLE FUNCTION")
print("-" * 60)

def create_user(username, *roles, **attributes):
    """Create user with username, roles, and custom attributes."""
    user = {
        'username': username,
        'roles': roles,
        'attributes': attributes
    }
    return user

user1 = create_user('alice', 'admin', 'editor', email='alice@example.com', verified=True)
print(f"User 1: {user1}")

user2 = create_user('bob', 'user', phone='555-1234', newsletter=False)
print(f"User 2: {user2}")

# ============================================================================
# 9. COUNTING ARGUMENTS
# ============================================================================
print("\n\n9. COUNTING ARGUMENTS")
print("-" * 60)

def count_args(*args, **kwargs):
    """Count positional and keyword arguments."""
    print(f"  Positional arguments (*args): {len(args)}")
    print(f"  Keyword arguments (**kwargs): {len(kwargs)}")
    print(f"  Total: {len(args) + len(kwargs)}")

print("Counting with count_args(1, 2, 3, name='Alice', age=30):")
count_args(1, 2, 3, name='Alice', age=30)

# ============================================================================
# 10. FILTERING WITH *args AND **kwargs
# ============================================================================
print("\n\n10. FILTERING WITH *args AND **kwargs")
print("-" * 60)

def filter_data(*numbers, **options):
    """Filter numbers based on options."""
    result = list(numbers)
    
    if options.get('even'):
        result = [n for n in result if n % 2 == 0]
    
    if options.get('positive'):
        result = [n for n in result if n > 0]
    
    if 'min' in options:
        result = [n for n in result if n >= options['min']]
    
    return result

print("filter_data(1, 2, 3, 4, 5, -1, -2, even=True):")
print(f"  Result: {filter_data(1, 2, 3, 4, 5, -1, -2, even=True)}")

print("\nfilter_data(1, 2, 3, 4, 5, -1, -2, positive=True):")
print(f"  Result: {filter_data(1, 2, 3, 4, 5, -1, -2, positive=True)}")

print("\nfilter_data(1, 2, 3, 4, 5, -1, -2, min=2):")
print(f"  Result: {filter_data(1, 2, 3, 4, 5, -1, -2, min=2)}")

# ============================================================================
# 11. ARGUMENTS WITH DEFAULT VALUES
# ============================================================================
print("\n\n11. ARGUMENTS WITH DEFAULT VALUES")
print("-" * 60)

def build_url(domain, *paths, protocol='https', port=None):
    """Build URL from domain, paths, and options."""
    url = f"{protocol}://{domain}"
    
    if port:
        url += f":{port}"
    
    for path in paths:
        url += f"/{path}"
    
    return url

print("build_url('example.com', 'api', 'users'):")
print(f"  {build_url('example.com', 'api', 'users')}")

print("\nbuild_url('example.com', 'api', 'users', protocol='http', port=8080):")
print(f"  {build_url('example.com', 'api', 'users', protocol='http', port=8080)}")

# ============================================================================
# 12. PRACTICAL EXAMPLE: LOGGER
# ============================================================================
print("\n\n12. PRACTICAL EXAMPLE: LOGGER")
print("-" * 60)

def log_message(level, *messages, **options):
    """Log message with level and custom options."""
    timestamp = options.get('timestamp', True)
    separator = options.get('separator', ' | ')
    
    message = separator.join(str(m) for m in messages)
    
    if timestamp:
        from datetime import datetime
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{time_str}] [{level.upper()}] {message}")
    else:
        print(f"[{level.upper()}] {message}")

print("Logger examples:")
log_message('info', 'Application', 'started', 'successfully')
log_message('error', 'Database', 'connection', 'failed', timestamp=False)
log_message('warning', 'High memory usage detected', separator=' -> ')

print("\n" + "=" * 60)
print("END OF *args AND **kwargs TUTORIAL")
print("=" * 60)
