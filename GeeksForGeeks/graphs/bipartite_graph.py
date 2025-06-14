#!/usr/bin/env python3
from typing import List, Optional, Dict, Any, Tuple
import sys
import os
from collections import deque
from pathlib import Path

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
    """Write result to output file or console, handling various data types"""
    # Handle different data types appropriately
    if isinstance(result, list) or isinstance(result, tuple):
        # Check if it's a 2D matrix/array
        if result and (isinstance(result[0], list) or isinstance(result[0], tuple)):
            # Format 2D matrix - each row on a new line
            output_str = '\n'.join([' '.join(map(str, row)) for row in result])
        else:
            # Format 1D array - space-separated values
            output_str = ' '.join(map(str, result))
    else:
        # For scalar values (int, str, etc.)
        output_str = str(result)
    
    # Write to file and/or console
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
    def isBipartite(self, V, edges) -> bool:
        """Given a Graph with V vertices (Numbered from 0 to V-1) and E edges. Check whether the graph is bipartite or not.

        A bipartite graph can be colored with two colors such that no two adjacent vertices share the same color. This means we can divide the graph’s vertices into two distinct sets where:

        All edges connect vertices from one set to vertices in the other set.
        No edges exist between vertices within the same set."""
        adj_list = self.create_adj_list(edges)
        colored_array = [-1 for _ in range(V)]

        for i in range(V):
            if colored_array[i] == -1:
                isBipartite = self.traverse(i, adj_list, colored_array)
                if not isBipartite:
                    return False
                
        return True

    def traverse(self, src, adj_list, colored_array):
        q = deque()
        q.append(src)
        colored_array[src] = 0

        if src not in adj_list:
            colored_array[src] = 0
            return True


        while len(q) > 0:
            cur_vertex = q.popleft()

            for neighbour in adj_list[cur_vertex]:
                if colored_array[neighbour] == -1:
                    q.append(neighbour)
                    colored_array[neighbour] = 1 if colored_array[cur_vertex] == 0 else 0
                elif colored_array[cur_vertex] == colored_array[neighbour]:
                    return False
                
        return True

    def create_adj_list(self, edges):
        adj_list = {}
        for frm, to in edges:
            if frm not in adj_list:
                adj_list[frm] = []
            adj_list[frm].append(to)

            if to not in adj_list:
                adj_list[to] = []
            adj_list[to].append(frm)

        return adj_list


def main():
    setup_io()
    
    try:
        # Parse input for the problem
        # TODO: Parse input
        n = read_int()
        m = read_int()
        edges = [ read_list_int() for _ in range(m)]
        
        # Create solution object and call the function
        solution = Solution()
        result = solution.isBipartite(n, edges)
        
        # Output result
        write_output(result)
    
    finally:
        cleanup_io()

if __name__ == "__main__":
    main()