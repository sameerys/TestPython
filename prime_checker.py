def is_prime(number):
    """
    Check if a given number is prime.
    
    A prime number is a natural number greater than 1 that is only divisible by 1 and itself.
    This function uses an optimized algorithm that:
    1. Handles special cases (numbers < 2, 2, even numbers)
    2. For odd numbers, only checks divisibility up to the square root
    
    Args:
        number (int): The number to check for primality
            Must be an integer (positive or negative)
            Boolean values are not accepted even though they are subclass of int
    
    Returns:
        bool: True if the number is prime, False otherwise
            Returns False for:
            - Numbers less than 2 (including negative numbers)
            - Even numbers except 2
            - Numbers with odd divisors up to their square root
    
    Raises:
        TypeError: If the input is not an integer (e.g., float, string, list, bool)
    
    Examples:
        >>> is_prime(17)
        True
        >>> is_prime(4)
        False
        >>> is_prime(1)
        False
        >>> is_prime(2)  # Only even prime number
        True
        >>> is_prime(-7)  # Negative numbers are not prime
        False
        >>> is_prime(997)  # Large prime number
        True
    
    Note:
        - Zero is not prime by definition
        - One is not prime by definition
        - Negative numbers are not prime by definition
        - Two is the only even prime number
    """
    if type(number) is not int:
        raise TypeError("Input must be an integer")
    # Handle special cases
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Check odd numbers up to the square root of number
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True

# Example usage
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 17, 20, 97]
    print("Testing various numbers for primality:")
    for num in test_numbers:
        print(f"{num:3d} is{' ' if is_prime(num) else ' not '}prime")
    
    print("\nTesting edge cases:")
    print(f"Is -7 prime? {is_prime(-7)}")  # False (negative number)
    print(f"Is 0 prime? {is_prime(0)}")    # False (zero)
    print(f"Is 1 prime? {is_prime(1)}")    # False (one is not prime by definition)
    print(f"Is 2 prime? {is_prime(2)}")    # True (only even prime number)
    
    try:
        is_prime(3.14)  # Will raise TypeError
    except TypeError as e:
        print("\nError handling example:")
        print(f"is_prime(3.14) -> {str(e)}")
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 17, 20, 97]
    for num in test_numbers:
        print(f"{num} is{' ' if is_prime(num) else ' not '}prime")
