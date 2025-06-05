# Simplified LeetCode Template Usage

This template is designed for solving LeetCode problems locally with a focus on single test cases and simplified input parsing.

## Features

- Single test case processing (vs. multiple test cases)
- Helper functions for parsing different data types
- Built-in data structures (TreeNode, ListNode)
- Easy to use as a VS Code snippet
- **Input/Output file support** - read from input.txt, write to output.txt (falls back to console)

## How to Use the Template

1. Copy `leetcode_template.py` to your solution directory
2. Modify the input parsing section in `main()` to read your specific inputs
3. Implement your solution in the `Solution` class
4. Run with `python leetcode_template.py`

### Input Options

The template will automatically:
1. Try to read input from `input.txt` if it exists
2. Otherwise, prompt for input via console
3. Try to write output to `output.txt`
4. Always display output in the console

### Example

For a problem like "Two Sum" where you need an array and a target:

```python
def main():
    setup_io()  # Sets up file/console I/O
    
    try:
        # Input parsing
        nums = read_list_int()  # [2, 7, 11, 15]
        target = read_int()     # 9
        
        # Solution execution
        solution = Solution()
        result = solution.twoSum(nums, target)
        
        # Output
        write_output(result)  # Writes to file and console
    finally:
        cleanup_io()  # Closes any open files
```

## Available Helper Functions

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

## File Input/Output

### Input File Format

The `input.txt` file should contain each input value on a separate line:

```
2 7 11 15
9
```

For the Two Sum problem, this represents:
- Line 1: The array of numbers (space-separated)
- Line 2: The target value

### Output File

Results will be written to `output.txt` in the following format:

```
[0, 1]
```

## Using as a VS Code Snippet

1. Open VS Code
2. Go to File > Preferences > User Snippets
3. Select Python (or create a new global snippet file)
4. Copy the contents of `leetcode_vscode_snippet.json` into your snippets file
5. Save the file

Now you can use the snippet in your Python files by typing `leetcode` and pressing Tab or Enter.

### VS Code Snippet Fields

The snippet includes tab stops for easy navigation:

1. `method_name` - Name of your solution method
2. `parameters` - Method parameters with types
3. `# TODO: Implement solution` - Placeholder for your implementation
4. `pass` - Placeholder for your code
5. `# TODO: Parse input` - Placeholder for input parsing
6. `# Example: nums = read_list_int()` - Example input parsing
7. `# Example: target = read_int()` - Example input parsing
8. `arguments` - Arguments to pass to your solution method

## Workflow

1. Create a new Python file
2. Type `leetcode` and press Tab to insert the template
3. Fill in the method name and parameters
4. Implement your solution
5. Update the input parsing section
6. Create an `input.txt` file with your test case (optional)
7. Run the file with `python your_solution.py`

## Example Input/Output

For the Two Sum problem:

**Input (input.txt):**
```
2 7 11 15
9
```

**Code:**
```python
def main():
    setup_io()
    try:
        nums = read_list_int()
        target = read_int()
        
        solution = Solution()
        result = solution.twoSum(nums, target)
        
        write_output(result)
    finally:
        cleanup_io()
```

**Output (output.txt and console):**
```
[0, 1]
``` 