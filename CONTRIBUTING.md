# Contributing Guide

This guide explains how to add new solutions to this repository.

## Adding a New Solution

### Step 1: Choose the Correct Directory

Place your solution in the appropriate platform and difficulty directory:
- For LeetCode: `LeetCode/{Easy,Medium,Hard}/`
- For Codeforces: `Codeforces/{Div1,Div2,Educational}/`
- For other platforms: Use their respective directories

### Step 2: File Naming Convention

Follow the platform-specific naming conventions:
- LeetCode: `LC_<problem_number>_<problem_name>.<extension>`
- Codeforces: `CF_<contest_number><problem_letter>_<problem_name>.<extension>`
- HackerRank: `HR_<problem_name>.<extension>`
- CodeChef: `CC_<problem_code>_<problem_name>.<extension>`
- AtCoder: `AC_<contest_name><problem_letter>_<problem_name>.<extension>`
- SPOJ: `SPOJ_<problem_code>_<problem_name>.<extension>`

### Step 3: Include Problem Information

Start your solution with a comment block containing:
```
/**
 * Problem: <problem_number/code>. <problem_title>
 * Difficulty: <difficulty_level>
 * Link: <problem_link>
 * 
 * Time Complexity: O(?)
 * Space Complexity: O(?)
 * 
 * Description:
 * <brief_problem_description>
 */
```

### Step 4: Write Clean and Documented Code

- Use proper indentation
- Include comments explaining non-trivial logic
- Optimize your solution for time and space complexity
- Include alternative approaches if applicable

### Step 5: Update Progress Tracker

After adding your solution:
1. Update the `progress_tracker.md` file
2. Update relevant README statistics

## Folder Structure

If you need to add a new platform, follow this structure:
```
NewPlatform/
├── README.md           # Platform info and statistics
├── Category1/          # Platform-specific categories
├── Category2/
└── ...
```

## Code Style Guidelines

- Use consistent formatting
- Follow language-specific best practices
- Keep solutions clear and readable
- Include test cases when possible 