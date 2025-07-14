import os
import sys
from collections import deque
from typing import List, Tuple, Union, TextIO, Optional, Any

# --- Global File Objects ---
# These will be initialized once the root directory is found.
_input_file: Optional[TextIO] = None
_output_file: Optional[TextIO] = None

def _find_project_root() -> str:
    """
    Dynamically finds the project root directory.
    It looks for a marker file/directory (like '.git' or 'utils.py')
    by traversing up from the current script's directory.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    marker_files = ['.git', 'utils.py', 'input.txt'] # Add other markers if you have them

    # Loop upwards until a marker file/directory is found or we hit the system root
    while True:
        for marker in marker_files:
            if os.path.exists(os.path.join(current_dir, marker)):
                return current_dir
        
        parent_dir = os.path.dirname(current_dir)
        if parent_dir == current_dir: # Reached filesystem root
            raise FileNotFoundError("Project root not found. Make sure 'utils.py' or '.git' is in your root directory.")
        current_dir = parent_dir

def _initialize_io():
    """
    Initializes global input and output file objects.
    This function should be called once, typically when the module is loaded.
    """
    global _input_file, _output_file
    if _input_file is None: # Only initialize if not already done
        root_dir = _find_project_root()
        
        input_path = os.path.join(root_dir, 'input.txt')
        output_path = os.path.join(root_dir, 'output.txt')

        try:
            _input_file = open(input_path, 'r')
            # Open output in write mode. 'w' truncates the file each time.
            # Use 'a' for append if you want to keep previous outputs.
            _output_file = open(output_path, 'w')
        except IOError as e:
            print(f"Error opening I/O files: {e}", file=sys.stderr)
            sys.exit(1) # Exit if essential files can't be opened

    # Register a cleanup function to close files when the program exits
    import atexit
    atexit.register(_cleanup_io)

def _cleanup_io():
    """Closes the global input and output file objects."""
    global _input_file, _output_file
    if _input_file:
        _input_file.close()
        _input_file = None
    if _output_file:
        _output_file.close()
        _output_file = None

# Automatically initialize I/O when the module is imported
# _initialize_io()


# --- Common Input Reading Functions ---

def read_line() -> str:
    """Reads a single line from input.txt and strips whitespace."""
    if _input_file:
        return _input_file.readline().strip()
    return "" # Should not happen if _initialize_io works

def read_int() -> int:
    """Reads a single integer from input.txt."""
    return int(read_line())

def read_string() -> str:
    """Reads a single string (token) from input.txt."""
    return read_line()

def read_ints(separator: str = ' ') -> List[int]:
    """Reads a line of space-separated integers from input.txt into a list."""
    return [int(x) for x in read_line().split(separator)]

def read_strings(separator: str = ' ') -> List[str]:
    """Reads a line of space-separated strings from input.txt into a list."""
    return read_line().split(separator)

def read_char_matrix() -> List[List[str]]:
    """Reads a matrix of characters (e.g., '0', '1', '#', '.')"""
    matrix = []
    while True:
        line = read_line()
        if not line: # Empty line signals end of matrix or input
            break
        matrix.append(list(line))
    return matrix

def read_int_matrix() -> List[List[int]]:
    """Reads a matrix of integers (each row is space-separated)."""
    matrix = []
    while True:
        line = read_line()
        if not line: # Empty line signals end of matrix or input
            break
        matrix.append([int(x) for x in line.split()])
    return matrix

# --- Common Output Writing Functions ---

def write_line(content: Any, end: str = '\n'):
    """Writes content to output.txt followed by a newline."""
    if _output_file:
        _output_file.write(str(content) + end)

def write_int(number: int):
    """Writes an integer to output.txt followed by a newline."""
    write_line(number)

def write_string(s: str):
    """Writes a string to output.txt followed by a newline."""
    write_line(s)

def write_list(lst: List[Any], separator: str = ' '):
    """Writes a list of items to output.txt, separated by 'separator', followed by a newline."""
    write_line(separator.join(map(str, lst)))


IS_LOCAL_TESTING = True
if IS_LOCAL_TESTING:
    _initialize_io()
else:
    _input_file = sys.stdin
    _output_file = sys.stdout