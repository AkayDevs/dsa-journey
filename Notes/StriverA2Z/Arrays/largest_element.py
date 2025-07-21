import collections
import heapq
import math
from typing import List, Tuple, Dict, Set, Optional, Any

# --- Import I/O Utilities ---
try:
    from DSA.utils import ( # type: ignore
        read_int, read_ints, read_string, read_strings,
        read_char_matrix, read_int_matrix,
        write_line, write_int, write_string, write_list
    )
except ImportError:
    import sys
    import os
    current_script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root_found = False
    temp_path = current_script_dir
    for _ in range(5): # Check up to 5 parent directories to find 'utils.py'
        if os.path.exists(os.path.join(temp_path, 'utils.py')):
            sys.path.insert(0, temp_path)
            project_root_found = True
            break
        temp_path = os.path.dirname(temp_path)
        if temp_path == current_script_dir: # Reached filesystem root
            break
    
    if not project_root_found:
        raise ImportError("Could not find 'utils.py'. Ensure it's in a discoverable parent directory.")

    from utils import (
        read_int, read_ints, read_string, read_strings,
        read_char_matrix, read_int_matrix,
        write_line, write_int, write_string, write_list
    )

# --- Problem Description ---
'''
Given an array, we have to find the largest element in the array.
'''

# --- Example Test Cases ---
'''
Example 1:
Input: arr[] = {2,5,1,3,0};
Output: 5
Explanation: 5 is the largest element in the array. 

Example2: 
Input: arr[] = {8,10,5,7,9};
Output: 10
Explanation: 10 is the largest element in the array. 
'''

# --- Solution ---

class Solution:
    def solve(self, nums) -> Any:
        """
        Consider edge cases:
        - Empty inputs
        - Single element inputs
        - Constraints on input values (e.g., negative numbers, large numbers)
        
        Time Complexity: O(N)
        Space Complexity: O(1)
        """
        # --- Algorithm Implementation ---
        max_elem = float('-inf')
        for cur_elem in nums:
            if cur_elem > max_elem:
                max_elem = cur_elem

        return max_elem

# --- Main Execution for Testing ---
if __name__ == "__main__":
    solver = Solution()

    # Define test cases and use I/O functions
    # Example for Two Sum problem (assuming input.txt has N, then N space-separated ints, then target):
    # N = read_int()
    # nums = read_ints()
    # target = read_int()
    # result = solver.solve(nums, target) # Replace .solve with your actual method name
    # write_list(result)

    # Example for a simple print:
    # write_line("Hello from solution!")

    # Add direct assert statements for quick local validation:
    # assert solver.solve(input_args) == expected_output, "Test Case X Failed!"
    
    print("\n--- Testing Complete ---")
    print("Check 'output.txt' in the root directory for results.")