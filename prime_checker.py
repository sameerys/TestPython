def is_prime(number):
    """
    Check if a given number is prime.
    
    Args:
        number (int): The number to check
    
    Returns:
        bool: True if the number is prime, False otherwise
        
    Raises:
        TypeError: If the input is not an integer    """
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
    for num in test_numbers:
        print(f"{num} is{' ' if is_prime(num) else ' not '}prime")
