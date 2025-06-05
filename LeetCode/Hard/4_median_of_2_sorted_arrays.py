#!/usr/bin/env python3
from typing import List, Optional, Dict, Any
from collections import deque

# ----- Input/Output Setup -----

input_file = None
output_file = None
input_lines = []
line_index = 0

def setup_io():
    """Setup input and output sources"""
    global input_file, output_file, input_lines, line_index
    # Try to open input file
    try:
        input_file = open('input.txt', 'r')
        input_lines = input_file.readlines()
        print(f"Reading input from input.txt ({len(input_lines)} lines)")
    except FileNotFoundError:
        print("No input.txt found, reading from console")
    
    # Try to open output file
    try:
        output_file = open('output.txt', 'w')
        print("Writing output to output.txt")
    except:
        print("Could not open output.txt, writing to console")

def cleanup_io():
    """Close open files"""
    if input_file:
        input_file.close()
    if output_file:
        output_file.close()

def read_line() -> str:
    """Read a line from input file or console"""
    global line_index
    if input_lines:
        if line_index < len(input_lines):
            line = input_lines[line_index].strip()
            line_index += 1
            return line
        else:
            raise EOFError("Reached end of input file")
    else:
        return input().strip()

def write_output(result):
    """Write result to output file or console"""
    output_str = str(result)
    if output_file:
        output_file.write(output_str + '\n')
    print(output_str)

# ----- Helper Functions for Parsing Input -----

def read_int() -> int:
    """Read a single integer from input"""
    return int(read_line())

def read_float() -> float:
    """Read a single float from input"""
    return float(read_line())

def read_str() -> str:
    """Read a single string from input"""
    return read_line()

def read_list_int() -> List[int]:
    """Read a list of integers from input"""
    return list(map(int, read_line().split()))

def read_list_float() -> List[float]:
    """Read a list of floats from input"""
    return list(map(float, read_line().split()))

def read_list_str() -> List[str]:
    """Read a list of strings from input"""
    return read_line().split()

def read_grid(rows: int) -> List[List[int]]:
    """Read a grid of integers with the specified number of rows"""
    return [read_list_int() for _ in range(rows)]

def read_grid_char(rows: int) -> List[List[str]]:
    """Read a grid of characters with the specified number of rows"""
    return [list(read_line()) for _ in range(rows)]

# ----- Data Structure Definitions -----

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# ----- Solution Class -----

class Solution:
    def findMedianSortedArrays(self, nums1 : List[int], nums2: List[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        
        if n1 > n2 : 
            return self.findMedianSortedArrays(nums2, nums1)
        
        n_total = n1 + n2
        n_left = (n_total + 1) / 2
        
        low, high = 0, n1

        while (low <= high):
            mid1 = (high + low + 1) // 2
            mid2 = n_left - mid1

            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')

            if mid1 < n1 : 
                r1 = nums1[int(mid1)]
            if mid2 < n2 :
                r2 = nums2[int(mid2)]
            if mid1 - 1 >= 0:
                l1 = nums1[int(mid1 - 1)]
            if mid2 - 1 >= 0 : 
                l2 = nums2[int(mid2 - 1)]

            if l1 <= r2 and l2 <= r1: 
                return max(l1, l2) if n_total % 2 == 1 else (max(l1, l2) + min(r1, r2)) / 2
            elif l1 > r2 :
                high = mid1 - 1
            else :
                low = mid1 + 1
        return 0

def main():
    setup_io()
    
    try:
        # ----- Input Parsing -----
        nums1 = read_list_int()
        nums2 = read_list_int()
        
        # ----- Solution Execution -----
        solution = Solution()
        result = solution.findMedianSortedArrays(nums1, nums2)
        
        # ----- Output Formatting -----
        write_output(result)
    finally:
        cleanup_io()

if __name__ == "__main__":
    main()