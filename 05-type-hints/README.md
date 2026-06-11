# 05 - Type Hints

## Overview
This project covers Python type hints (annotations):
- Basic type hints for functions and variables
- Type hints with collections
- Complex type hints
- The typing module
- Type checking with mypy
- Protocols and generics

## 📋 Topics Covered

### Basic Type Hints
- Function parameter types
- Return type annotations
- Variable type annotations
- Optional types

### Collections and Complex Types
- Typing lists, tuples, dicts, sets
- Union types
- Literal types
- TypeVar and generics

### Advanced Typing
- Protocols
- Callable types
- Type aliases
- Forward references

### Type Checking
- Using mypy for static type checking
- Finding type errors
- Type checking tools

## 📁 Files

- `01_basic_type_hints.py` - Function and variable annotations
- `02_advanced_type_hints.py` - Complex type hints
- `03_typing_module.py` - Using the typing module
- `examples/` - Real-world examples

## 🎯 Key Concepts

### Basic Type Hints
```python
def add(a: int, b: int) -> int:
    """Add two integers and return the result."""
    return a + b

# Variable type hints
name: str = "Alice"
age: int = 25
height: float = 5.7
```

### Optional Types
```python
from typing import Optional

def greet(name: Optional[str] = None) -> str:
    if name is None:
        return "Hello!"
    return f"Hello, {name}!"
```

### Collections
```python
from typing import List, Dict, Set, Tuple

# List of integers
numbers: List[int] = [1, 2, 3]

# Dictionary with string keys and integer values
ages: Dict[str, int] = {"Alice": 30, "Bob": 25}

# Set of strings
tags: Set[str] = {"python", "coding", "tutorial"}

# Tuple with specific types
coordinates: Tuple[int, int] = (10, 20)
```

### Union Types
```python
from typing import Union

# Can be either int or str
def process(value: Union[int, str]) -> str:
    return str(value).upper()
```

### Generic Types
```python
from typing import TypeVar, Generic, List

T = TypeVar('T')

def first_element(items: List[T]) -> T:
    return items[0]
```

## 🚀 Running the Files

```bash
python 01_basic_type_hints.py
python 02_advanced_type_hints.py
python 03_typing_module.py

# Type check with mypy
mypy 01_basic_type_hints.py
```

## ✏️ Exercises

1. Add type hints to your previous function examples
2. Create a function that takes and returns List[Dict[str, int]]
3. Use Optional types appropriately
4. Create a generic function using TypeVar
5. Use Union types for flexible function parameters

## 📚 Resources

- [Type Hints](https://docs.python.org/3/library/typing.html)
- [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [Static Type Checking](https://docs.python.org/3/library/typing.html)
