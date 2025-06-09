# GeeksforGeeks Python Template

A robust template for solving GeeksforGeeks (GFG) problems locally with convenient file I/O and helper functions.

## Features

- Multiple test case handling (GFG standard format)
- File-based input/output with hierarchical search (local directory → project root)
- Helper functions for parsing different data types
- Common data structures (Node for linked lists, TreeNode for binary trees)
- VS Code snippet for quick setup

## Template Structure

The template follows GeeksforGeeks' standard problem format:
1. A first line containing the number of test cases (`T`)
2. For each test case, problem-specific input format
3. Solution function with the signature required by GFG
4. Output for each test case

## How to Use

### Basic Usage

1. Copy `gfg_template.py` to your solution directory
2. Implement your solution in the `Solution` class
3. Modify the input parsing in the `main()` function to match the problem's input format
4. Run with `python gfg_template.py`

### Input/Output Options

The template provides flexible I/O handling:

- **Input Search Order**:
  1. First looks for `input.txt` in the current directory
  2. Then looks for `input.txt` in the project root directory
  3. Falls back to console input if no file is found

- **Output Search Order**:
  1. First tries to write to `output.txt` in the current directory
  2. Then tries to write to `output.txt` in the project root directory
  3. Falls back to console-only output if no file can be created

This allows you to have a global input/output file at the project root while still supporting local files for specific problems.

### Project Root Configuration

The template automatically determines the project root as the parent directory of the current file. If you need to customize this, modify the `PROJECT_ROOT` variable:

```python
# Custom project root
PROJECT_ROOT = Path('/path/to/your/project/root')
```

### Example

For a problem like "Find maximum in array":

```python
def main():
    setup_io()
    
    try:
        # Read number of test cases
        t = read_int()
        
        for _ in range(t):
            # For each test case, read array size and elements
            n = read_int()
            arr = read_list_int()
            
            # Call solution function
            solution = Solution()
            result = solution.findMax(arr, n)
            
            # Output result
            write_output(result)
    finally:
        cleanup_io()
```

## Input Parsing Functions

| Function | Description | Example Input | Result |
|----------|-------------|--------------|--------|
| `read_int()` | Read a single integer | `42` | `42` |
| `read_float()` | Read a single float | `3.14` | `3.14` |
| `read_str()` | Read a single string | `hello` | `"hello"` |
| `read_list_int()` | Read a list of integers | `1 2 3 4` | `[1, 2, 3, 4]` |
| `read_list_float()` | Read a list of floats | `1.1 2.2 3.3` | `[1.1, 2.2, 3.3]` |
| `read_list_str()` | Read a list of strings | `a b c` | `["a", "b", "c"]` |
| `read_grid(rows)` | Read a grid of integers | `1 2 3`<br>`4 5 6` | `[[1, 2, 3], [4, 5, 6]]` |
| `read_grid_char(rows)` | Read a grid of characters | `abc`<br>`def` | `[["a", "b", "c"], ["d", "e", "f"]]` |

## Data Structures

The template includes common data structures used in GeeksforGeeks problems:

### Linked List

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
```

Helper functions:
- `build_linked_list(arr)`: Build a linked list from an array
- `print_linked_list(head)`: Convert linked list to array for printing

### Binary Tree

```python
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
```

Helper functions:
- `build_tree(arr)`: Build a binary tree from an array (level order)
- `inorder_traversal(root)`: Get inorder traversal of binary tree

## Using as a VS Code Snippet

1. Open VS Code
2. Go to File > Preferences > User Snippets
3. Select Python (or create a new global snippet file)
4. Copy the contents of `gfg_vscode_snippet.json` into your snippets file
5. Save the file

Now you can use the snippet in your Python files by typing `gfg` and pressing Tab or Enter.

### VS Code Snippet Fields

The snippet includes tab stops for easy navigation:

1. `function_name` - Name of your solution function
2. `parameters` - Function parameters
3. `return_type` - Return type of the function
4. `Function description` - Documentation for your function
5. `# TODO: Implement your solution` - Placeholder for your implementation
6. `pass` - Placeholder for your code
7. `# TODO: Parse input for this test case` - Placeholder for input parsing
8. `# Example: n = read_int()` - Example input parsing
9. `# Example: arr = read_list_int()` - Example input parsing
10. `arguments` - Arguments to pass to your solution function

## Sample Input/Output

For a "Find maximum in array" problem:

**Input (input.txt in current directory or project root):**
```
2
5
1 2 3 4 5
3
5 10 15
```

This represents:
- 2 test cases
- First test case: array of 5 elements [1, 2, 3, 4, 5]
- Second test case: array of 3 elements [5, 10, 15]

**Solution code:**
```python
class Solution:
    def findMax(self, arr, n):
        """Find maximum element in array"""
        if not arr:
            return -1
        return max(arr)
```

**Output (output.txt in current directory or project root and console):**
```
5
15
``` 