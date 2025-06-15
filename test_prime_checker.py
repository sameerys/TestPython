"""
Test suite for the prime_checker.py module.

This test suite verifies the functionality of the is_prime() function with various test cases:

Test Categories:
1. test_negative_numbers:
   - Verifies that negative numbers are correctly identified as not prime
   - Tests: -1, -2, -17

2. test_zero_and_one:
   - Verifies that 0 and 1 are correctly identified as not prime
   - These are special cases in number theory

3. test_small_primes:
   - Verifies known small prime numbers are correctly identified
   - Tests prime numbers from 2 to 31
   - Includes first few prime numbers: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31

4. test_small_composites:
   - Verifies small composite numbers are correctly identified as not prime
   - Tests composite numbers from 4 to 20
   - Includes numbers like 4 (2×2), 6 (2×3), 8 (2×4), etc.

5. test_large_primes:
   - Verifies larger prime numbers are correctly identified
   - Tests prime numbers up to 997
   - Includes primes like 97, 101, 103, 107, 997

6. test_perfect_squares:
   - Verifies perfect square numbers (except 4) are correctly identified as not prime
   - Tests squares from 4 to 100
   - Special case: 4 is both a perfect square and composite

7. test_type_errors:
   - Verifies function properly handles invalid input types
   - Tests various non-integer inputs: floats, strings, lists, tuples, booleans
   - Ensures TypeError is raised for invalid inputs

Usage:
    Run all tests: python -m unittest test_prime_checker.py
    Run with detailed output: python -m unittest test_prime_checker.py -v

Note: Each test case uses subTest context manager for better reporting when
      multiple assertions within a single test method fail.
"""

import unittest
from prime_checker import is_prime

class TestPrimeChecker(unittest.TestCase):
    def test_negative_numbers(self):
        """Test that negative numbers are not prime"""
        self.assertFalse(is_prime(-1))
        self.assertFalse(is_prime(-2))
        self.assertFalse(is_prime(-17))

    def test_zero_and_one(self):
        """Test that 0 and 1 are not prime"""
        self.assertFalse(is_prime(0))
        self.assertFalse(is_prime(1))

    def test_small_primes(self):
        """Test small prime numbers"""
        known_small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
        for prime in known_small_primes:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime))

    def test_small_composites(self):
        """Test small composite numbers"""
        known_composites = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for composite in known_composites:
            with self.subTest(composite=composite):
                self.assertFalse(is_prime(composite))

    def test_large_primes(self):
        """Test some larger prime numbers"""
        known_large_primes = [97, 101, 103, 107, 997]
        for prime in known_large_primes:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime))

    def test_perfect_squares(self):
        """Test perfect squares (which are composite except for 4)"""
        perfect_squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
        for square in perfect_squares:
            with self.subTest(square=square):
                self.assertFalse(is_prime(square))

    def test_type_errors(self):
        """Test that non-integer inputs raise TypeError"""
        invalid_inputs = [1.5, "2", [3], (4,), True, False]
        for invalid in invalid_inputs:
            with self.subTest(invalid=invalid):
                with self.assertRaises(TypeError):
                    is_prime(invalid)

if __name__ == '__main__':
    unittest.main()