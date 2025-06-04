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

# ----- TreeNode Definition for Binary Tree Problems -----

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_list(nodes: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a binary tree from a list of values (LeetCode format)"""
    if not nodes:
        return None
    root = TreeNode(nodes[0])
    queue = deque([root])
    i = 1
    while queue and i < len(nodes):
        node = queue.popleft()
        # Left child
        if i < len(nodes) and nodes[i] is not None:
            node.left = TreeNode(nodes[i])
            queue.append(node.left)
        i += 1
        # Right child
        if i < len(nodes) and nodes[i] is not None:
            node.right = TreeNode(nodes[i])
            queue.append(node.right)
        i += 1
    return root

# ----- ListNode Definition for Linked List Problems -----

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list_from_list(values: List[int]) -> Optional[ListNode]:
    """Build a linked list from a list of values"""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert a linked list to a list of values"""
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values

# ----- Solution Class -----

class Solution:
    # Implement your solution here
    def example_method(self, nums: List[int], target: int) -> List[int]:
        # Example implementation (Two Sum)
        num_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]
            num_map[num] = i
        return []  # No solution found

def main():
    setup_io()
    
    try:
        # ----- Input Parsing (Customize this section) -----
        # Example: Reading inputs for Two Sum problem
        nums = read_list_int()
        target = read_int()
        
        # ----- Solution Execution -----
        solution = Solution()
        # Change the method name and parameters to match your problem
        result = solution.example_method(nums, target)
        
        # ----- Output Formatting -----
        write_output(result)
    finally:
        cleanup_io()

if __name__ == "__main__":
    main() 