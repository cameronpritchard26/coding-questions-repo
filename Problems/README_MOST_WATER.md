# Container With Most Water Problem

[Back to problems](../README.md)

## Problem Description

Problem source: [LeetCode Container With Most Water](https://leetcode.com/problems/container-with-most-water/)

Given an array of integers `height` where each element represents the height of a vertical line at that position, find two lines that together with the x-axis form a container that holds the most water. Return the maximum amount of water the container can store.

### Rules
1. The width of the container is determined by the distance between the two lines
2. The height of the container is limited by the shorter of the two lines
3. Area = `min(height[i], height[j]) * (j - i)` where `i` and `j` are the indices of the two lines
4. You cannot slant the container (the water level must be horizontal)

### Constraints
- 2 ≤ n ≤ 10^5, where n is the length of the height array
- 0 ≤ height[i] ≤ 10^6

### Examples

**Example 1:**
```
Height: [1, 8, 6, 2, 5, 4, 8, 3, 7]

Visual representation:
8 |   █     █
7 |   █     █   █
6 |   █ █   █   █
5 |   █ █ █ █   █
4 |   █ █ █ █ █ █
3 |   █ █ █ █ █ █ █
2 |   █ █ █ █ █ █ █
1 | █ █ █ █ █ █ █ █ █
  +-------------------
    0 1 2 3 4 5 6 7 8

Best container: Between index 1 (height=8) and index 8 (height=7)
- Width: 8 - 1 = 7
- Height: min(8, 7) = 7
- Area: 7 × 7 = 49

Result: 49
```

**Example 2:**
```
Height: [1, 1]

Only one possible container between indices 0 and 1.
- Width: 1 - 0 = 1
- Height: min(1, 1) = 1
- Area: 1 × 1 = 1

Result: 1
```

**Example 3:**
```
Height: [4, 3, 2, 1, 4]

Best container: Between index 0 (height=4) and index 4 (height=4)
- Width: 4 - 0 = 4
- Height: min(4, 4) = 4
- Area: 4 × 4 = 16

Result: 16
```

**Example 4:**
```
Height: [100, 1, 1, 1, 1, 1, 1, 1, 1, 100]

Best container: Between index 0 (height=100) and index 9 (height=100)
- Width: 9 - 0 = 9
- Height: min(100, 100) = 100
- Area: 9 × 100 = 900

Result: 900
```

## Solution Logic

The solution uses an **optimal two-pointer algorithm** to find the maximum area in a single pass through the array.

### Algorithm Overview

**Phase 1: Initialization**
- Set `left` pointer to index 0 (leftmost line)
- Set `right` pointer to index n-1 (rightmost line)
- Initialize `max_area = 0`

**Phase 2: Two-Pointer Traversal**

While `left < right`:

1. **Calculate Current Area**:
   - `current_area = min(height[left], height[right]) * (right - left)`
   - Update `max_area = max(max_area, current_area)`

2. **Move Pointer Strategically**:
   - If `height[left] < height[right]`: increment `left` pointer
   - Else: decrement `right` pointer

**Phase 3: Return Result**
- Return `max_area`

### Key Design Decisions

1. **Why Move the Shorter Line?**
   - The area is limited by the shorter line
   - Moving the taller line can only decrease width while keeping height the same or worse
   - Moving the shorter line gives a chance to find a taller line that might compensate for the reduced width

2. **Greedy Strategy Correctness**:
   - Starting with maximum width ensures we don't miss the optimal solution
   - Each move eliminates all possibilities involving the moved pointer at its current position
   - The algorithm guarantees we consider the optimal pair

3. **Why This Works**:
   ```
   Example: height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
   
   Start: left=0 (h=1), right=8 (h=7)
   Area = min(1,7) × 8 = 8
   Move left (shorter) → left=1
   
   left=1 (h=8), right=8 (h=7)
   Area = min(8,7) × 7 = 49 ← Best!
   Move right (shorter) → right=7
   
   Continue until left meets right...
   ```

### Complexity Analysis

**Time Complexity: O(n)**
- Single pass through the array with two pointers
- Each iteration moves one pointer closer to the other
- At most n iterations
- Optimal - must examine each line at least once

**Space Complexity: O(1)**
- Only constant extra space used (two pointers, two variables)
- No additional data structures needed
- Optimal - minimal memory footprint

### Why This Solution Is Optimal

This solution is **already optimal** and cannot be improved asymptotically:

1. **Must examine every line**: Any solution requires considering each line at least once to ensure we don't miss the optimal container
2. **Minimal space usage**: Only tracks two pointers and the current maximum
3. **Single pass**: Processes the array in O(n) time with no redundant operations
4. **Greedy correctness**: The two-pointer strategy guarantees finding the optimal solution

**Alternative approaches considered:**
- **Brute force**: Check all pairs - O(n²) time - strictly worse
- **Divide and conquer**: Would still be O(n log n) or worse - no benefit
- **Dynamic programming**: No overlapping subproblems - unnecessary overhead
- **Sorting-based**: Would destroy positional information needed for width calculation

**Why brute force doesn't work efficiently:**
```python
# Brute force: O(n²)
for i in range(n):
    for j in range(i+1, n):
        area = min(height[i], height[j]) * (j - i)
        max_area = max(max_area, area)
```
This checks all n(n-1)/2 pairs, but the two-pointer approach intelligently skips pairs that cannot be optimal.

## Implementation

### Function Signature

```python
def maxArea(height) -> int
```

**Parameters:**
- `height`: List of integers representing the heights of vertical lines

**Returns:**
- Integer representing the maximum area of water that can be contained

### Example Usage

```python
from most_water import maxArea

# Example with optimal container in middle
print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# Output: 49

# Simple case
print(maxArea([1, 1]))
# Output: 1

# Symmetric case
print(maxArea([4, 3, 2, 1, 4]))
# Output: 16

# High values at ends
print(maxArea([100, 1, 1, 1, 1, 1, 1, 1, 1, 100]))
# Output: 900

# Strictly increasing
print(maxArea([1, 2, 3, 4, 5]))
# Output: 6

# Strictly decreasing
print(maxArea([5, 4, 3, 2, 1]))
# Output: 6
```

## Testing

The solution includes comprehensive test coverage with 20 test cases.

### Test Coverage
- ✓ Edge cases (two elements, all equal heights)
- ✓ Boundary conditions (strictly increasing/decreasing sequences)
- ✓ Symmetric patterns (equal heights at both ends)
- ✓ Asymmetric patterns (peaks in middle, at ends)
- ✓ Long sequences (testing performance)
- ✓ Large value differences (0 to 10^6)
- ✓ Complex patterns with multiple local maxima
- ✓ Constraint adherence (array lengths from 2 to large values)

### Running Tests

**Full test suite:**
```bash
python Testing/test_most_water.py
```

### Test Results

All 20 tests pass with 100% success rate:
```
============================================================
Results: 20/20 tests passed
============================================================
```

## Files

- [**`most_water.py`**](../Code/most_water.py) - Main solution implementation
- [**`test_most_water.py`**](../Testing/test_most_water.py) - Comprehensive test suite (20 tests)
