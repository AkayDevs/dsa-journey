#!/usr/bin/env python3
from stress_test import ArrayStressTest, StressTest
import random
import time

"""
This file demonstrates how to use the stress test framework with various algorithm examples.
"""

# Example 1: Testing sorting algorithms
def bubble_sort(array):
    """A simple bubble sort implementation (inefficient)"""
    arr = array.copy()  # Don't modify the original
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def optimized_sort(array):
    """Using Python's built-in sort (efficient)"""
    return sorted(array)

def test_sorting():
    """Compare bubble sort with Python's built-in sort"""
    print("\n=== Testing Sorting Algorithms ===")
    
    # Create a custom validator since sorting results need special comparison
    def validator(result1, result2):
        """Custom validator function to compare sorted arrays"""
        if len(result1) != len(result2):
            return False
        return all(a == b for a, b in zip(result1, result2))
    
    class SortingStressTest(ArrayStressTest):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.validator = validator  # Use our custom validator
            
        def run_test(self, test_data):
            result = {
                "test_data": test_data,
                "solution_result": None,
                "reference_result": None,
                "solution_time_ms": 0,
                "reference_time_ms": 0,
                "error": None
            }
            
            # Run solution implementation
            try:
                start_time = time.time()
                result["solution_result"] = self.solution_func(**test_data)
                end_time = time.time()
                result["solution_time_ms"] = (end_time - start_time) * 1000
            except Exception as e:
                result["error"] = f"Solution error: {str(e)}"
                return False, result
                
            # Time limit check
            if result["solution_time_ms"] > self.time_limit_ms:
                return False, result
                
            # Run reference implementation
            if self.reference_func:
                try:
                    start_time = time.time()
                    result["reference_result"] = self.reference_func(**test_data)
                    end_time = time.time()
                    result["reference_time_ms"] = (end_time - start_time) * 1000
                    
                    # Compare results using our custom validator
                    if not self.validator(result["solution_result"], result["reference_result"]):
                        return False, result
                except Exception as e:
                    result["error"] = f"Reference error: {str(e)}"
                    return False, result
                    
            return True, result
    
    # Run the test with small arrays first
    tester = SortingStressTest(
        solution_func=bubble_sort,
        reference_func=optimized_sort,
        test_count=5,
        time_limit_ms=1000,
        min_size=1,
        max_size=100,
        min_value=-1000,
        max_value=1000,
        verbose=True
    )
    
    print("Testing with small arrays:")
    tester.run_tests()
    
    # Now test with larger arrays to demonstrate time limit failures
    print("\nTesting with larger arrays (likely to exceed time limit):")
    tester = SortingStressTest(
        solution_func=bubble_sort,
        reference_func=optimized_sort,
        test_count=3,
        time_limit_ms=50,  # Small time limit to demonstrate timeout
        min_size=1000,
        max_size=2000,
        min_value=-1000,
        max_value=1000,
        verbose=True
    )
    tester.run_tests()


# Example 2: Testing binary search algorithm
def binary_search(array, target):
    """Binary search implementation"""
    arr = sorted(array)  # Ensure array is sorted
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1  # Not found

def linear_search(array, target):
    """Linear search implementation (reference solution)"""
    arr = sorted(array)  # Ensure array is sorted
    for i, num in enumerate(arr):
        if num == target:
            return i
    return -1  # Not found

def test_binary_search():
    """Test binary search vs linear search"""
    print("\n=== Testing Binary Search ===")
    
    class SearchStressTest(StressTest):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
        def generate_test(self):
            """Generate a test case for search algorithms"""
            array_size = random.randint(1, 1000)
            array = [random.randint(-1000, 1000) for _ in range(array_size)]
            
            # Choose target that may or may not be in the array
            if random.random() < 0.8:  # 80% chance target exists in array
                target = random.choice(array)
            else:  # 20% chance target doesn't exist
                target = random.randint(-2000, 2000)
                
            return {
                "array": array,
                "target": target
            }
    
    # Run the tests
    tester = SearchStressTest(
        solution_func=binary_search,
        reference_func=linear_search,
        test_count=20,
        time_limit_ms=100,
        verbose=True
    )
    
    tester.run_tests()


# Example 3: Testing string manipulation
def is_palindrome_optimized(string):
    """Check if a string is a palindrome (optimized)"""
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(ch.lower() for ch in string if ch.isalnum())
    # Compare string with its reverse
    return cleaned == cleaned[::-1]

def is_palindrome_reference(string):
    """Check if a string is a palindrome (reference implementation)"""
    # Convert to lowercase and remove non-alphanumeric characters
    cleaned = ''.join(ch.lower() for ch in string if ch.isalnum())
    # Two-pointer approach
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

def test_palindrome():
    """Test palindrome checking functions"""
    print("\n=== Testing Palindrome Checker ===")
    
    class PalindromeStressTest(StressTest):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
        
        def generate_test(self):
            """Generate palindrome test cases"""
            # Generate random string with mix of characters
            length = random.randint(1, 100)
            chars = "abcdefghijklmnopqrstuvwxyz0123456789 !@#$%^&*()-_=+[]{};:,.<>/?"
            
            if random.random() < 0.5:  # 50% chance of palindrome
                # Generate a palindrome
                half_length = length // 2
                first_half = ''.join(random.choice(chars) for _ in range(half_length))
                mid_char = '' if length % 2 == 0 else random.choice(chars)
                string = first_half + mid_char + first_half[::-1]
            else:
                # Generate a random string (likely not a palindrome)
                string = ''.join(random.choice(chars) for _ in range(length))
                
            return {"string": string}
    
    # Run the tests
    tester = PalindromeStressTest(
        solution_func=is_palindrome_optimized,
        reference_func=is_palindrome_reference,
        test_count=50,
        time_limit_ms=100,
        verbose=True
    )
    
    tester.run_tests()


if __name__ == "__main__":
    print("Running example stress tests for various algorithms")
    test_sorting()
    test_binary_search()
    test_palindrome() 