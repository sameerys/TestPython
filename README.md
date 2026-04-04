# TestPython

A collection of Python learning scripts and utilities for practicing Python programming concepts.

## Project Structure

```
TestPython/
├── src/                      # Python source code
│   ├── __init__.py          # Package initializer
│   ├── prime_checker.py     # Prime number checker module
│   ├── test_prime_checker.py # Unit tests for prime checker
│   └── dictionary.py        # Dictionary learning examples
├── README.md                # This file
└── index.html              # Project index page
```

## Modules

### 1. Prime Number Checker (`src/prime_checker.py`)

An efficient prime number checker with advanced optimizations and comprehensive error handling.

**Features:**
- Efficiently checks if a given number is prime
- Uses 6k±1 optimization for better performance
- Handles edge cases and validates input types
- Protects against extremely large numbers
- Comprehensive unit test suite with 13 test cases

**Usage:**
```python
from src.prime_checker import is_prime

# Check if a number is prime
print(is_prime(17))  # True
print(is_prime(4))   # False
print(is_prime(97))  # True
```

**Running the module directly:**
```bash
cd src
python prime_checker.py
```

**Function Details:**

The `is_prime()` function takes an integer as input and returns:
- `True` if the number is prime
- `False` if the number is not prime
- Raises `TypeError` if input is not an integer
- Raises `ValueError` if number is too large (> 10^12)

### 2. Dictionary Examples (`src/dictionary.py`)

A comprehensive tutorial program demonstrating Python dictionary operations.

**Topics Covered:**
- Creating dictionaries
- Accessing values ([] notation and get() method)
- Adding and modifying key-value pairs
- Removing items (pop, del, clear)
- Checking key existence
- Iterating through dictionaries (keys, values, items)
- Dictionary methods (len, keys, values)
- Nested dictionaries
- Dictionary comprehension
- Creating dictionaries from lists (zip)
- Copying dictionaries

**Usage:**
```bash
cd src
python dictionary.py
```

### 3. Test Suite (`src/test_prime_checker.py`)

Comprehensive unit tests for the prime checker module covering:
- Negative numbers
- Zero and one
- Small and large primes
- Composite numbers
- Perfect squares
- Mersenne primes
- Carmichael numbers
- Twin primes
- Type validation
- Boundary conditions

**Running tests:**
```bash
cd src
python -m unittest test_prime_checker.py -v
```

## Getting Started

1. Clone the repository
2. Navigate to the project directory
3. Run any module from the `src` folder

**Example:**
```bash
cd src
python dictionary.py
```

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses standard library only)

## Testing

Run all unit tests:
```bash
cd src
python -m unittest test_prime_checker.py -v
```

Expected output: 13 tests passed

## Examples

### Prime Checker Example
```python
from src.prime_checker import is_prime

# Test with different numbers
test_numbers = [1, 2, 3, 4, 5, 17, 20, 97]
for num in test_numbers:
    print(f"{num} is{' ' if is_prime(num) else ' not '}prime")
```

**Output:**
```
1 is not prime
2 is prime
3 is prime
4 is not prime
5 is prime
17 is prime
20 is not prime
97 is prime
```

### Dictionary Example
```python
# Creating a dictionary
student = {
    "name": "John Doe",
    "age": 20,
    "grade": "A"
}

# Accessing values
print(student["name"])  # John Doe
print(student.get("email", "Not available"))  # Not available

# Adding items
student["email"] = "john@example.com"

# Iterating
for key, value in student.items():
    print(f"{key}: {value}")
```

## License

This project is for educational purposes.
