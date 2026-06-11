# 🚀 SAMPLE PROJECTS - Core Python

This file contains real-world sample projects that integrate concepts from all 5 Core Python modules. Each project demonstrates practical applications of variables, functions, *args/**kwargs, list comprehensions, generators, and type hints.

---

## 📌 Project 1: Student Grade Management System

**Topics**: Variables, Functions, *args/**kwargs, Type Hints, List Comprehensions

A comprehensive system to manage student grades, calculate statistics, and generate reports.

### Features:
- Add students with their grades
- Calculate average, min, max grades
- Filter students by grade range
- Generate grade reports
- Support for multiple subjects

### Code Structure:
```python
from typing import List, Dict, Tuple

def add_students(*names: str, **grades: float) -> Dict[str, float]:
    """Add multiple students with their grades."""
    pass

def calculate_statistics(*scores: float) -> Dict[str, float]:
    """Calculate mean, median, std dev of scores."""
    pass

def filter_top_performers(students: List[Dict], threshold: float) -> List[Dict]:
    """Filter students with grades above threshold using list comprehension."""
    pass

def generate_report(**student_data: Dict) -> str:
    """Generate formatted grade report."""
    pass
```

### Key Concepts:
- Function parameters and return types
- *args for variable student names
- **kwargs for flexible grade input
- Type hints with Dict, List, Tuple
- List comprehensions for filtering

---

## 📌 Project 2: File Processing with Generators

**Topics**: Generators, Yield, List Comprehensions, Type Hints

Process large log files efficiently using generators to avoid loading everything into memory.

### Features:
- Read large files line by line
- Filter log entries by level (INFO, ERROR, WARNING)
- Parse structured log data
- Generate statistics about logs
- Memory-efficient processing

### Code Structure:
```python
from typing import Generator, Iterator
from pathlib import Path

def read_large_file(filepath: Path) -> Generator[str, None, None]:
    """Read file line by line using generator."""
    pass

def filter_logs(log_generator: Generator, level: str) -> Generator[str, None, None]:
    """Filter logs by level using generator."""
    pass

def parse_log_entry(line: str) -> Dict[str, str]:
    """Parse structured log entry."""
    pass

def generate_statistics(log_file: Path) -> Dict[str, int]:
    """Generate statistics using generator."""
    pass
```

### Key Concepts:
- Generator functions with yield
- Memory efficiency with lazy evaluation
- Type hints with Generator and Iterator
- List comprehensions for data extraction

---

## 📌 Project 3: Data Analysis Pipeline

**Topics**: Functions, List Comprehensions, Dictionaries, Type Hints

Build a data analysis pipeline with filtering, transformation, and aggregation.

### Features:
- Load CSV-like data
- Filter records by criteria
- Transform data using comprehensions
- Group data by categories
- Calculate aggregations (sum, avg, count)

### Code Structure:
```python
from typing import List, Dict, Any, Optional

def load_data(filename: str) -> List[Dict[str, Any]]:
    """Load data from file."""
    pass

def filter_records(data: List[Dict], **criteria: Any) -> List[Dict]:
    """Filter records matching criteria using **kwargs."""
    pass

def transform_data(data: List[Dict]) -> List[Dict]:
    """Transform data using list comprehensions."""
    pass

def aggregate_by_category(data: List[Dict], category: str) -> Dict[str, List]:
    """Group and aggregate data by category."""
    pass

def calculate_statistics(*values: float) -> Dict[str, float]:
    """Calculate statistics for any number of values."""
    pass
```

### Key Concepts:
- List and dict comprehensions
- *args for flexible calculations
- **kwargs for flexible filtering
- Type hints with Optional and Any

---

## 📌 Project 4: Configuration Management System

**Topics**: Variables, Functions, *args/**kwargs, Type Hints, Dictionaries

Create a flexible configuration system that supports multiple sources and formats.

### Features:
- Load config from multiple sources
- Validate configuration values
- Support nested configurations
- Environment variable overrides
- Configuration merging

### Code Structure:
```python
from typing import Dict, Any, Union

class ConfigManager:
    def __init__(self):
        self.config: Dict[str, Any] = {}
    
    def load_config(self, *sources: str, **overrides: Any) -> None:
        """Load config from multiple sources with overrides."""
        pass
    
    def get_value(self, key: str, default: Any = None) -> Any:
        """Get config value with type hint."""
        pass
    
    def validate_config(self, **required_keys: type) -> bool:
        """Validate config has required keys."""
        pass
    
    def merge_configs(*configs: Dict) -> Dict:
        """Merge multiple config dictionaries."""
        pass
```

### Key Concepts:
- Class structure with type hints
- *args for multiple sources
- **kwargs for configuration overrides
- Dictionary operations and merging

---

## 📌 Project 5: Data Streaming Analytics

**Topics**: Generators, Functions, Type Hints, List Comprehensions

Process streaming data (like sensor readings) using generators.

### Features:
- Simulate data stream with generator
- Real-time filtering and transformation
- Calculate rolling statistics
- Detect anomalies
- Buffer and batch processing

### Code Structure:
```python
from typing import Generator, List, Tuple
from collections import deque

def generate_sensor_data(duration: int) -> Generator[float, None, None]:
    """Generate simulated sensor readings."""
    pass

def filter_by_range(stream: Generator, min_val: float, max_val: float) -> Generator[float, None, None]:
    """Filter values in range using generator."""
    pass

def calculate_rolling_average(stream: Generator, window_size: int) -> Generator[float, None, None]:
    """Calculate rolling average using generator."""
    pass

def detect_anomalies(stream: Generator, threshold: float) -> Generator[Tuple[float, bool], None, None]:
    """Detect anomalies in data stream."""
    pass

def batch_process(stream: Generator, batch_size: int) -> Generator[List[float], None, None]:
    """Batch streaming data for processing."""
    pass
```

### Key Concepts:
- Generator chaining
- Type hints with complex types
- Rolling window calculations
- Memory-efficient streaming

---

## 📌 Project 6: Web API Response Handler

**Topics**: Functions, *args/**kwargs, Type Hints, List Comprehensions, Dictionaries

Build a handler for parsing and processing web API responses.

### Features:
- Parse JSON responses
- Extract specific fields using comprehensions
- Handle nested data structures
- Error handling and validation
- Support multiple API formats

### Code Structure:
```python
from typing import Dict, List, Any, Optional
import json

def parse_api_response(response: str) -> Dict[str, Any]:
    """Parse JSON API response."""
    pass

def extract_fields(data: Dict, *keys: str) -> Dict[str, Any]:
    """Extract specific fields from response using *args."""
    pass

def transform_response(data: Dict, **transformations: callable) -> Dict:
    """Apply transformations to response fields."""
    pass

def filter_results(data: List[Dict], **filters: Any) -> List[Dict]:
    """Filter API results using **kwargs and list comprehensions."""
    pass

def flatten_nested(data: Dict, prefix: str = "") -> Dict[str, Any]:
    """Flatten nested response structure."""
    pass
```

### Key Concepts:
- JSON parsing with type hints
- *args for multiple field extraction
- **kwargs for flexible transformations
- List comprehensions for filtering

---

## 📌 Project 7: Report Generator

**Topics**: Generators, Functions, Type Hints, List/Dict Comprehensions

Generate formatted reports from structured data using all Core Python concepts.

### Features:
- Process data streams with generators
- Generate formatted sections
- Calculate summaries and statistics
- Create tables and charts (text-based)
- Support multiple output formats

### Code Structure:
```python
from typing import Generator, List, Dict, Any
from datetime import datetime

def load_data_stream(source: str) -> Generator[Dict[str, Any], None, None]:
    """Load data as stream using generator."""
    pass

def generate_section(title: str, *rows: Dict, **options: Any) -> str:
    """Generate report section with *args/**kwargs."""
    pass

def create_table(data: List[Dict], columns: List[str]) -> str:
    """Create formatted table using list comprehensions."""
    pass

def calculate_summary(data: Generator) -> Dict[str, Any]:
    """Calculate summary statistics from data stream."""
    pass

def format_report(*sections: str, **metadata: Any) -> str:
    """Format final report from sections."""
    pass
```

### Key Concepts:
- Generator for data streaming
- Type hints for complex types
- *args and **kwargs for flexibility
- List/dict comprehensions for data transformation

---

## 🎯 Getting Started with Projects

### Steps:
1. Choose a project that interests you
2. Create a new Python file for the project
3. Implement the functions with proper type hints
4. Add error handling
5. Test with sample data
6. Enhance with additional features

### Tips:
- Start with Project 1 for fundamentals
- Progress to more complex projects
- Combine multiple projects for larger systems
- Add proper documentation and docstrings
- Write unit tests for your functions

---

## 📚 Integration Chart

| Project | Variables | Functions | *args/**kwargs | Comprehensions | Generators | Type Hints |
|---------|-----------|-----------|----------------|-----------------|-----------|-----------|
| 1. Student Grades | ✓ | ✓ | ✓ | ✓ | - | ✓ |
| 2. File Processing | ✓ | ✓ | - | ✓ | ✓ | ✓ |
| 3. Data Analysis | ✓ | ✓ | ✓ | ✓ | - | ✓ |
| 4. Configuration | ✓ | ✓ | ✓ | - | - | ✓ |
| 5. Stream Analytics | ✓ | ✓ | - | ✓ | ✓ | ✓ |
| 6. API Handler | ✓ | ✓ | ✓ | ✓ | - | ✓ |
| 7. Report Generator | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

---

## 🔗 Project Dependencies

```
Project 1 (Student Grades) → Foundation project
     ↓
Project 2 (File Processing) → Uses concepts from Project 1
     ↓
Project 3 (Data Analysis) → Combines Projects 1 & 2
     ↓
Project 4 (Configuration) → Supports all projects
     ↓
Project 5 (Stream Analytics) → Advanced processing
     ↓
Project 6 (API Handler) → Real-world application
     ↓
Project 7 (Report Generator) → Capstone project combining all
```

---

## 💡 Extension Ideas

1. **Add Database Integration**: Store and retrieve data
2. **Add CLI Interface**: Command-line arguments with argparse
3. **Add Web Interface**: Flask/Django integration
4. **Add Testing**: Unit tests with pytest
5. **Add Logging**: Structured logging for all projects
6. **Add Performance**: Benchmark different approaches
7. **Add Visualization**: Charts and graphs with matplotlib

---

## 📝 Notes

- Each project builds on previous concepts
- All projects use type hints (best practice!)
- Error handling is important for production code
- Consider edge cases and validation
- Write docstrings for all functions
- Test your code thoroughly

Happy Learning! 🐍
