#!/usr/bin/env python3
# Link : https://www.geeksforgeeks.org/problems/flood-fill-algorithm1856/1
from typing import List, Optional, Dict, Any, Tuple
import sys
import os
from pathlib import Path
from queue import Queue

# ----- Input/Output Setup -----

input_file = None
output_file = None
input_lines = []
line_index = 0

# Project root directory - modify this if needed
# This can also be determined using environment variables or by searching for common project files
PROJECT_ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent

def setup_io():
    """Setup input and output sources, checking both local and project root directories"""
    global input_file, output_file, input_lines, line_index
    
    # Try to open input file (first in current directory, then in project root)
    current_dir_input = Path('input.txt')
    root_dir_input = PROJECT_ROOT / 'input.txt'
    
    try:
        # Try current directory first
        if current_dir_input.exists():
            input_file = open(current_dir_input, 'r')
            print(f"Reading input from {current_dir_input}")
        # Then try project root
        elif root_dir_input.exists():
            input_file = open(root_dir_input, 'r')
            print(f"Reading input from {root_dir_input}")
        else:
            print("No input.txt found in current directory or project root, reading from console")
        
        # If we opened a file, read all lines
        if input_file:
            input_lines = input_file.readlines()
            print(f"Read {len(input_lines)} lines from input file")
    except Exception as e:
        print(f"Error opening input file: {e}")
        print("Reading from console")
    
    # Try to open output file (first in current directory, then in project root)
    current_dir_output = Path('output.txt')
    root_dir_output = PROJECT_ROOT / 'output.txt'
    
    try:
        # Try current directory first
        if os.access(os.path.dirname(current_dir_output.absolute()), os.W_OK):
            output_file = open(current_dir_output, 'w')
            print(f"Writing output to {current_dir_output}")
        # Then try project root
        elif os.access(os.path.dirname(root_dir_output.absolute()), os.W_OK):
            output_file = open(root_dir_output, 'w')
            print(f"Writing output to {root_dir_output}")
        else:
            print("Could not open output.txt in current directory or project root, writing to console only")
    except Exception as e:
        print(f"Error opening output file: {e}")
        print("Writing to console only")

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
    else: 
        print("No output file found.")
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

# Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Binary Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# ----- Solution Class -----

class Solution:
    """
    Your solution implementation goes here.
    For GeeksforGeeks, implement the function with the exact signature they require.
    """
    def floodFill(self, image, sr, sc, newColor):
        n = len(image)
        m = len(image[0])
        visited_array = [[0 for _ in range(m)] for _ in range(n)]
        original_color = image[sr][sc]

        q = Queue()
        q.put_nowait((sr, sc))

        possible_coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while not q.empty():
            cur_point = q.get_nowait()
            sr, sc = cur_point
            visited_array[sr][sc] = 1
            image[sr][sc] = newColor

            for coord in possible_coords:
                delta_row, delta_col = coord
                new_sr = delta_row + sr
                new_sc = delta_col + sc
                if new_sr >= 0 and new_sr < n and new_sc >= 0 and new_sc < m and visited_array[new_sr][new_sc] != 1 and image[new_sr][new_sc] == original_color:
                    q.put_nowait((new_sr, new_sc))
                    
        return image

            

def main():
    setup_io()
    
    try:
        n = read_int()
        m = read_int()
        image = read_grid(n)
        sr, sc = read_list_int()
        newColor = read_int()
        
        # Create solution object and call the function
        solution = Solution()
        result = solution.floodFill(image, sr, sc, newColor)
        
        # Output result for this test case
        write_output(result)
    
    finally:
        cleanup_io()

if __name__ == "__main__":
    main()