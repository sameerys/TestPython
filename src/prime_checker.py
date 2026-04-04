def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if the number is prime, False otherwise
        
    Raises:
        TypeError: If the input is not an integer
        ValueError: If the input is too large to process efficiently
        OverflowError: If the input causes mathematical overflow
    """
    if type(number) is not int:
        raise TypeError("Input must be an integer")
    
    # Check for extremely large numbers that could cause performance issues
    if number > 10**12:
        raise ValueError("Number too large for efficient prime checking")
    
    # Handle special cases
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    
    # Additional optimization: check divisibility by 3
    if number == 3:
        return True
    if number % 3 == 0:
        return False
    
    # Use 6k±1 optimization: all primes > 3 are of form 6k±1
    try:
        limit = int(number ** 0.5) + 1
        for i in range(5, limit, 6):
            if number % i == 0 or number % (i + 2) == 0:
                return False
    except OverflowError:
        raise OverflowError("Mathematical overflow occurred during prime checking")
    
    return True

# Example usage
if __name__ == "__main__":
    test_numbers = [1, 2, 3, 4, 5, 17, 20, 97]
    for num in test_numbers:
        print(f"{num} is{' ' if is_prime(num) else ' not '}prime")
