#!/usr/bin/env python3
from typing import List, Optional, Dict, Any
import sys
import os
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
    # Initial Approach - O(n^2)
    def trap(self, height: List[int]):
        total_water = 0
        left = 0
        n = len(height)

        while left != n - 1:
            max_iter_index, max_iter_height, water_displaced_till_max_iter = 0, -1, 0
            water_displaced = 0
            for right in range(left + 1, n):
                if height[right] >= height[left]:
                    max_iter_height = height[right]
                    max_iter_index = right
                    break
                else :
                    if height[right] > max_iter_height:
                        max_iter_height = height[right]
                        water_displaced_till_max_iter = water_displaced
                        max_iter_index = right
                    water_displaced += height[right]
            
            min_tower = min(height[left], max_iter_height)
            total_width = max_iter_index - left - 1
            water_displaced = water_displaced if max_iter_height >= height[left] else water_displaced_till_max_iter
            total_water += max(0, ((min_tower * total_width) - water_displaced))
            left = max_iter_index

        return total_water
    
    def trapOptimised(self, height: List[int]) -> int:
        n = len(height)
        prefixMax = height.copy()
        suffixMax = height.copy()
        for i in range(1, n):
            prefixMax[i] = max(height[i], prefixMax[i - 1])
            suffixMax[n - i - 1] = max(height[n - i - 1], suffixMax[n - i])

        total_water = 0
        for tower in range(1, n - 1):
            water_on_tower = min(prefixMax[tower], suffixMax[tower]) - height[tower]
            total_water += water_on_tower
        
        return total_water
        


def main():
    setup_io()
    
    try:
        # ----- Input Parsing -----
        heights = read_list_int()
        
        # ----- Solution Execution -----
        solution = Solution()
        result = solution.trapOptimised(heights)
        
        # ----- Output Formatting -----
        write_output(result)
    finally:
        cleanup_io()

if __name__ == "__main__":
    main()