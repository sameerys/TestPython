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

    def test_large_number_limit(self):
        """Test that extremely large numbers raise ValueError"""
        large_numbers = [10**12 + 1, 10**15, 2**64]
        for large_num in large_numbers:
            with self.subTest(large_num=large_num):
                with self.assertRaises(ValueError):
                    is_prime(large_num)

    def test_boundary_values(self):
        """Test boundary values around the large number limit"""
        self.assertFalse(is_prime(10**12 - 1))  # 999999999999 is composite
        with self.assertRaises(ValueError):
            is_prime(10**12 + 1)  # Should raise ValueError

    def test_mersenne_primes(self):
        """Test known Mersenne primes (2^p - 1)"""
        mersenne_primes = [3, 7, 31, 127, 8191]  # 2^2-1, 2^3-1, 2^5-1, 2^7-1, 2^13-1
        for prime in mersenne_primes:
            with self.subTest(prime=prime):
                self.assertTrue(is_prime(prime))

    def test_carmichael_numbers(self):
        """Test Carmichael numbers (composite numbers that satisfy Fermat's test)"""
        carmichael_numbers = [561, 1105, 1729, 2465, 2821]
        for carmichael in carmichael_numbers:
            with self.subTest(carmichael=carmichael):
                self.assertFalse(is_prime(carmichael))

    def test_twin_primes(self):
        """Test twin prime pairs (primes that differ by 2)"""
        twin_prime_pairs = [(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
        for prime1, prime2 in twin_prime_pairs:
            with self.subTest(twin_pair=(prime1, prime2)):
                self.assertTrue(is_prime(prime1))
                self.assertTrue(is_prime(prime2))
                self.assertEqual(prime2 - prime1, 2)

    def test_optimization_edge_cases(self):
        """Test edge cases for the 6k±1 optimization"""
        # Test numbers of the form 6k+1 and 6k-1
        test_cases = [
            (5, True),   # 6*1-1
            (7, True),   # 6*1+1
            (11, True),  # 6*2-1
            (13, True),  # 6*2+1
            (25, False), # 6*4+1 but composite (5^2)
            (35, False), # 6*6-1 but composite (5*7)
        ]
        for number, expected in test_cases:
            with self.subTest(number=number):
                self.assertEqual(is_prime(number), expected)

if __name__ == '__main__':
    unittest.main()