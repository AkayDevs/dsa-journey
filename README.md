# Data Structures and Algorithms (DSA) Solutions

A collection of my solutions to various Data Structures and Algorithms problems from different competitive programming platforms.

## 📚 Repository Structure

```
DSA/
├── LeetCode/                 # LeetCode problems
│   ├── Easy/
│   ├── Medium/
│   └── Hard/
├── Codeforces/               # Codeforces problems
│   ├── Div1/
│   ├── Div2/
│   └── Educational/
├── HackerRank/               # HackerRank problems
├── CodeChef/                 # CodeChef problems
├── AtCoder/                  # AtCoder problems
├── SPOJ/                     # SPOJ problems
├── Templates/                # Template code for competitive programming
├── DataStructures/           # Implementation of various data structures
├── Algorithms/               # Implementation of various algorithms
└── Notes/                    # Notes on algorithms and data structures
```

## 🚀 Getting Started

Each problem solution contains:
- Problem statement/link
- Solution with time and space complexity analysis
- Alternative approaches (if applicable)

## 🔍 Navigation

- Navigate to specific platform folders to find problems from that platform
- Inside each platform, problems are organized by difficulty or contest category
- Search for problems by topic using the topic tags

## 📊 Statistics

- Total problems solved: 0
- LeetCode: 0
- Codeforces: 0
- HackerRank: 0
- CodeChef: 0
- AtCoder: 0
- SPOJ: 0

## 🔖 Topic Tags

- Arrays
- Strings
- Linked Lists
- Stacks
- Queues
- Trees
- Graphs
- Dynamic Programming
- Greedy Algorithms
- Backtracking
- Math
- Bit Manipulation
- Sorting and Searching
- Divide and Conquer
- Recursion 

# DSA Stress Testing Framework

A robust Python framework for stress testing data structures and algorithms solutions.

## Features

- Generate random test cases for common DSA problems (arrays, strings, graphs)
- Compare your optimized solution against a reference/naive implementation
- Time measurement and performance tracking
- Detailed error reporting for failed test cases
- Configurable test parameters (size, range, character set)

## Usage

### Basic Example

```python
from stress_test import ArrayStressTest

# Your optimized solution
def my_solution(array):
    return sum(array)
    
# Reference solution to compare against
def naive_solution(array):
    total = 0
    for num in array:
        total += num
    return total
    
# Create and run the stress test
tester = ArrayStressTest(
    solution_func=my_solution,
    reference_func=naive_solution,
    test_count=100,
    time_limit_ms=100,
    min_size=1,
    max_size=1000,
    min_value=-1000,
    max_value=1000,
    verbose=True
)

# Run the tests
tester.run_tests()

# Get failed tests for debugging
failed_tests = tester.get_failed_tests()
```

### Available Stress Test Classes

1. **ArrayStressTest** - For array-based problems
2. **StringStressTest** - For string manipulation problems
3. **GraphStressTest** - For graph algorithms

### Creating Custom Test Cases

You can extend the base `StressTest` class to create custom test generators:

```python
from stress_test import StressTest
import random

class TreeStressTest(StressTest):
    def __init__(
        self,
        solution_func,
        reference_func=None,
        test_count=100,
        time_limit_ms=1000,
        max_nodes=100,
        seed=None,
        verbose=False
    ):
        super().__init__(solution_func, reference_func, test_count, time_limit_ms, seed, verbose)
        self.max_nodes = max_nodes
        
    def generate_test(self):
        # Generate a random binary tree
        # This is a simplified example - you'd implement your own tree generation logic
        num_nodes = random.randint(1, self.max_nodes)
        nodes = list(range(1, num_nodes + 1))
        random.shuffle(nodes)
        
        # Create a tree structure (implementation depends on your problem)
        tree = nodes[0]  # Root
        
        return {"tree": tree}
```

## Running the Example

To run the included example:

```bash
python stress_test.py --example
```

## Customizing Test Generation

Override the `generate_test()` method in your subclass to create specific test patterns:

```python
def generate_test(self):
    # Generate test cases with specific edge cases
    if random.random() < 0.2:
        # 20% chance of generating empty array
        return {"array": []}
    elif random.random() < 0.3:
        # 30% chance of generating sorted array
        size = random.randint(self.min_size, self.max_size)
        array = sorted([random.randint(self.min_value, self.max_value) for _ in range(size)])
        return {"array": array}
    else:
        # Default: random array
        size = random.randint(self.min_size, self.max_size)
        array = [random.randint(self.min_value, self.max_value) for _ in range(size)]
        return {"array": array}
```

## Tips for Effective Testing

1. Start with small test cases and increase complexity gradually
2. Include edge cases in your test generation (empty arrays, single elements, etc.)
3. Use a simple but correct reference implementation for comparison
4. Save failed test cases for debugging
5. Use a fixed seed for reproducibility when debugging 

# LeetCode Problem Template

A simple, elegant template for working with LeetCode problems locally. The template handles input/output operations and allows you to focus on implementing the solution.

## Features

- Reads input from `input.txt` file or from terminal if the file doesn't exist
- Writes output to `output.txt` file or displays on terminal if writing fails
- Supports the standard LeetCode class/method format
- Handles JSON parsing for complex inputs
- Minimal dependencies (standard library only)

## Usage

### Setting Up

1. Copy the `leetcode_template.py` file to your solution directory
2. Update the `solution_method` and `solution_params` variables to match the LeetCode problem
3. Implement your solution in the `Solution` class
4. Create test cases in `input.txt` (one test case per line in JSON format)

### Example: Running a Solution

```bash
python leetcode_template.py
```

### Input Format

The `input.txt` file should contain one test case per line, with each line being a JSON array of the arguments for the solution method:

```
# For a method with two arguments (e.g., findMedianSortedArrays(nums1, nums2))
[[1,3],[2]]
[[1,2],[3,4]]
```

### Customizing for Different Problems

For a different LeetCode problem, update these sections in the template:

1. Update the problem configuration:
   ```python
   solution_method = "newMethodName"  # Method name from LeetCode
   solution_params = ["param1", "param2"]  # Parameter names in order
   ```

2. Implement the Solution class:
   ```python
   class Solution:
       def newMethodName(self, param1: Type1, param2: Type2) -> ReturnType:
           # Your solution here
           pass
   ```

## Example

For the "Median of Two Sorted Arrays" problem:

1. Template configuration:
   ```python
   solution_method = "findMedianSortedArrays"
   solution_params = ["nums1", "nums2"]
   ```

2. Solution implementation:
   ```python
   class Solution:
       def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
           # Your implementation here
   ```

3. Input file (input.txt):
   ```
   [[1,3],[2]]
   [[1,2],[3,4]]
   ```

4. Run the solution:
   ```bash
   python leetcode_template.py
   ```

5. Check output in `output.txt`:
   ```
   Case 1: 2.0
   Case 2: 2.5
   ``` 