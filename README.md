# coding-questions-repo
A repo for holding generated solutions to similar coding questions I've seen on tests

## Problems

### Additive Numbers

**File:** `additive_numbers.py`

#### Problem Description

An additive number is a number whose digits can be partitioned to form an additive sequence. A valid additive sequence must satisfy the following criteria:

1. The sequence contains at least three numbers
2. Each subsequent number in the sequence equals the sum of the previous two numbers
3. The first two numbers can be any valid partition of the initial digits

**Examples:**
- `112` is additive: `1 + 1 = 2` 
- `1123` is additive: `1 + 1 = 2, 1 + 2 = 3` 
- `1235` is additive: `1 + 2 = 3, 2 + 3 = 5` 
- `199100199` is additive: `1 + 99 = 100, 99 + 100 = 199` 
- `125` is NOT additive: `1 + 2 = 3` but next digit is `5`, not `3` 
- `198` is NOT additive: no valid partition exists 

#### Solution Logic

The solution uses a **brute-force partition approach** with validation:

**Phase 1: Partition Generation**
- Try all possible ways to split the number into a first and second number
- For a number with `n` digits, the first number can be 1 to n-2 digits long
- For each first number length `i`, the second number can be 1 to n-i-1 digits long
- This ensures at least one digit remains for the third number

**Phase 2: Sequence Validation**
- For each partition of the first two numbers:
  1. Calculate their sum to get the expected third number
  2. Check if the remaining digits start with this sum
  3. If yes, advance the position and repeat with the new pair (second + third)
  4. Continue until all digits are consumed or a mismatch occurs
  
**Phase 3: Leading Zero Handling**
- Numbers with leading zeros (except single `0`) are rejected
- This prevents invalid partitions like `01` or `00`

**Algorithm Complexity:**
- **Time:** O(n³) where n is the number of digits
  - O(n²) for trying all partition combinations
  - O(n) for validating each sequence
- **Space:** O(n) for string operations

#### Function Signature

```python
def isAdditiveNumber(num) -> bool
```

**Parameters:**
- `num`: An integer or string representing the number to check

**Returns:**
- `True` if the number is additive according to the rules
- `False` otherwise

**Example Usage:**
```python
>>> isAdditiveNumber(112)
True

>>> isAdditiveNumber(1123)
True

>>> isAdditiveNumber(125)
False

>>> isAdditiveNumber("199100199")
True