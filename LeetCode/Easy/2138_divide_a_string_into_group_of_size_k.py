#!/usr/bin/env python3
from typing import List, Optional, Dict, Any
import sys
import os
from collections import deque
from pathlib import Path

# ----- Input/Output Setup -----

input_file = None
output_file = None
input_lines = []
line_index = 0

PROJECT_ROOT = Path(os.path.dirname(os.path.abspath(__file__))).parent.parent

def setup_io():
    """Setup input and output sources"""
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
    
    current_dir_output = Path('output.txt')
    root_dir_output = PROJECT_ROOT / 'output.txt'
    
    try:
        # Check if output file exists in current directory
        if current_dir_output.exists():
            output_file = open(current_dir_output, 'a')
            print(f"Appending output to existing file {current_dir_output}")
        # Check if output file exists in project root
        elif root_dir_output.exists():
            output_file = open(root_dir_output, 'a')
            print(f"Appending output to existing file {root_dir_output}")
        # If no existing file found, try to create one in current directory
        elif os.access(os.path.dirname(current_dir_output.absolute()), os.W_OK):
            output_file = open(current_dir_output, 'w')
            print(f"Creating output file at {current_dir_output}")
        # Then try project root for creating new file
        elif os.access(os.path.dirname(root_dir_output.absolute()), os.W_OK):
            output_file = open(root_dir_output, 'w')
            print(f"Creating output file at {root_dir_output}")
        else:
            print("Could not open or create output.txt, writing to console only")
    except Exception as e:
        print(f"Error handling output file: {e}")
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
    def divideString(self, s: str, k: int, fill: str):
        n = len(s)
        filler_len = k - (n % k)
        new_str = s + filler_len * fill

        q = len(new_str) // k
        ans = []
        for i in range(q):
            ans.append(new_str[i: i + k + 1])

        return ans


def main():
    setup_io()
    
    try:
        # ----- Input Parsing -----
        # TODO: Parse input
        s = read_str()
        k = read_int()
        fill = read_str()
        
        # ----- Solution Execution -----
        solution = Solution()
        result = solution.divideString(s, k, fill)
        
        # ----- Output Formatting -----
        write_output(result)
    finally:
        cleanup_io()

if __name__ == "__main__":
    main()