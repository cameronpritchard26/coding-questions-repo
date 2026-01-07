# Additive Numbers Problem

[Back to problems](../README.md)

## Problem Description

An additive number is a number whose digits can be partitioned to form an additive sequence. A valid additive sequence must satisfy the following criteria:

### Rules
1. The sequence contains at least three numbers
2. Each subsequent number in the sequence equals the sum of the previous two numbers
3. The first two numbers can be any valid partition of the initial digits

### Examples

**Example 1:**
```
112 is additive: 1 + 1 = 2
```

**Example 2:**
```
1123 is additive: 1 + 1 = 2, 1 + 2 = 3
```

**Example 3:**
```
1235 is additive: 1 + 2 = 3, 2 + 3 = 5
```

**Example 4:**
```
199100199 is additive: 1 + 99 = 100, 99 + 100 = 199
```

**Example 5 (Not Additive):**
```
125 is NOT additive: 1 + 2 = 3 but next digit is 5, not 3
```

**Example 6 (Not Additive):**
```
198 is NOT additive: no valid partition exists
```

## Solution Logic

The solution uses a **brute-force partition approach** with validation to determine if a number is additive.

### Algorithm Overview

**Phase 1: Partition Generation**

- Try all possible ways to split the number into a first and second number
- For a number with `n` digits, the first number can be 1 to n-2 digits long
- For each first number length `i`, the second number can be 1 to n-i-1 digits long
- This ensures at least one digit remains for the third number

**Phase 2: Sequence Validation**

For each partition of the first two numbers:
1. Calculate their sum to get the expected third number
2. Check if the remaining digits start with this sum
3. If yes, advance the position and repeat with the new pair (second + third)
4. Continue until all digits are consumed or a mismatch occurs

**Phase 3: Leading Zero Handling**

- Numbers with leading zeros (except single `0`) are rejected
- This prevents invalid partitions like `01` or `00`

### Complexity Analysis

**Time Complexity: O(n³)**
- O(n²) for trying all partition combinations
- O(n) for validating each sequence
- Overall: O(n³) where n is the number of digits

**Space Complexity: O(n)**
- O(n) for string operations

## Implementation

### Function Signature

```python
def isAdditiveNumber(num) -> bool
```

**Parameters:**
- `num`: An integer or string representing the number to check

**Returns:**
- `True` if the number is additive according to the rules
- `False` otherwise

### Example Usage

```python
from additive_numbers import isAdditiveNumber

# Simple additive number
print(isAdditiveNumber(112))  # Output: True

# More complex additive number
print(isAdditiveNumber(1123))  # Output: True

# Not additive
print(isAdditiveNumber(125))  # Output: False

# Large additive number
print(isAdditiveNumber("199100199"))  # Output: True
```

## Testing

The solution includes comprehensive test coverage.

### Running Tests

**Full test suite:**
```bash
python test_additive_numbers.py
```

## Files

- [**`additive_numbers.py`**](../Code/additive_numbers.py) - Main solution implementation
- [**`test_additive_numbers.py`**](../Testing/test_additive_numbers.py) - Comprehensive test suite
