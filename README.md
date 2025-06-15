# TestPython
Test Scripts for Python Code
Updated for adding description.

## subheader
Watch tutorial on youtube

# Python Prime Number Checker

This project includes a simple and efficient function to check if a number is prime.

## Features

- Efficiently checks if a given number is prime
- Handles special cases (numbers less than 2, even numbers)
- Optimized to check only up to the square root of the input number

## Usage

```python
from prime_checker import is_prime

# Check if a number is prime
print(is_prime(17))  # True
print(is_prime(4))   # False
print(is_prime(1))   # False
print(is_prime(2))   # True
```

## Function Details

The `is_prime()` function takes an integer as input and returns:
- `True` if the number is prime
- `False` if the number is not prime

A prime number is a natural number greater than 1 that is only divisible by 1 and itself.

## Examples

```python
# Test with different numbers
test_numbers = [1, 2, 3, 4, 5, 17, 20, 97]
for num in test_numbers:
    print(f"{num} is{' ' if is_prime(num) else ' not '}prime")
```

Output:
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
