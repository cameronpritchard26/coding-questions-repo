# Breaking Records Problem

[Back to problems](../README.md)

## Problem Description

Problem source: [HackerRank Breaking Records](https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem)

A basketball player keeps a record of the number of points they scored in each game they played in, and they track the number of times they break their season record for most and least amount of points scored in a game. The number of points scored in the first game serves as the starting point for both records.

### Rules
1. The first game's score establishes the initial record for both maximum and minimum
2. A record is broken when a score is strictly greater than the current maximum or strictly less than the current minimum
3. Ties (equal scores) do NOT break records
4. Track both maximum and minimum record breaks separately

### Constraints
- 1 ≤ n ≤ 1000, where n is the number of scores
- 0 ≤ scores[i] ≤ 10^8

### Examples

**Example 1:**
```
Scores: [10, 5, 20, 20, 4, 5, 2, 25, 1]

Game 1: 10 → Initial record (max: 10, min: 10)
Game 2: 5 → Breaks min record (max: 10, min: 5) [0, 1]
Game 3: 20 → Breaks max record (max: 20, min: 5) [1, 1]
Game 4: 20 → No change (tie with max) [1, 1]
Game 5: 4 → Breaks min record (max: 20, min: 4) [1, 2]
Game 6: 5 → No change [1, 2]
Game 7: 2 → Breaks min record (max: 20, min: 2) [1, 3]
Game 8: 25 → Breaks max record (max: 25, min: 2) [2, 3]
Game 9: 1 → Breaks min record (max: 25, min: 1) [2, 4]

Result: [2, 4]
```

**Example 2:**
```
Scores: [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]

Game 1: 3 → Initial record
Game 2: 4 → Breaks max [1, 0]
Game 3: 21 → Breaks max [2, 0]
Game 4: 36 → Breaks max [3, 0]
Game 5: 10 → No change
Game 6: 28 → No change
Game 7: 35 → No change
Game 8: 5 → No change
Game 9: 24 → No change
Game 10: 42 → Breaks max [4, 0]

Result: [4, 0]
```

**Example 3:**
```
Scores: [10, 10, 10, 10]

All scores are the same, so no records are broken.

Result: [0, 0]
```

**Example 4:**
```
Scores: [1, 2, 3, 4, 5]

Strictly increasing sequence - only max records broken.

Result: [4, 0]
```

**Example 5:**
```
Scores: [5, 4, 3, 2, 1]

Strictly decreasing sequence - only min records broken.

Result: [0, 4]
```

## Solution Logic

The solution uses an **optimal single-pass algorithm** with running min/max tracking to count record breaks.

### Algorithm Overview

**Phase 1: Initialization**
- Set initial max and min records to the first game's score
- Initialize result array `[0, 0]` for `[max_breaks, min_breaks]`

**Phase 2: Sequential Processing**

For each score starting from the second game:

1. **Check Max Record**: If `score > max_score`:
   - Update `max_score = score`
   - Increment `result[0]` (max breaks counter)

2. **Check Min Record**: Else if `score < min_score`:
   - Update `min_score = score`
   - Increment `result[1]` (min breaks counter)

3. **No Change**: If `score == max_score` or `score == min_score` or `min_score < score < max_score`:
   - No records broken, continue to next score

**Phase 3: Return Result**
- Return `[max_breaks, min_breaks]`

### Key Design Decisions

1. **Using `elif` for Min Check**: Since a score cannot simultaneously break both max and min records, we use `elif` to avoid unnecessary comparisons

2. **No Separate Tracking Needed**: We only need to track the current max and min values, not the entire history

3. **First Game Handling**: Starting the loop from index 1 (second game) naturally handles the first game as the baseline

### Complexity Analysis

**Time Complexity: O(n)**
- Single pass through the array
- Constant-time operations per element
- Optimal - must examine each score at least once

**Space Complexity: O(1)**
- Only constant extra space used (two variables for min/max, one array for result)
- No additional data structures needed
- Optimal - minimal memory footprint

### Why This Solution Is Optimal

This solution is **already optimal** and cannot be improved asymptotically:

1. **Must examine every score**: Any solution requires looking at each score at least once to determine if records are broken
2. **Minimal space usage**: Only tracks two values (current min and max records)
3. **Single pass**: Processes each element exactly once with no redundant operations
4. **Early evaluation**: Uses `elif` to avoid unnecessary comparisons when max record is broken

**Alternative approaches considered:**
- **Two-pass solution**: Would be O(n) but slower in practice (2n operations vs n)
- **Sorting-based**: Would be O(n log n) - strictly worse
- **Additional data structures**: Would increase space complexity without improving time

## Implementation

### Function Signature

```python
def breaking_records(scores) -> list
```

**Parameters:**
- `scores`: List of integers representing points scored in each game

**Returns:**
- List of two integers `[max_breaks, min_breaks]` where:
  - `max_breaks` = number of times the maximum record was broken
  - `min_breaks` = number of times the minimum record was broken

### Example Usage

```python
from breaking_records import breaking_records

# Example with multiple breaks
print(breaking_records([10, 5, 20, 20, 4, 5, 2, 25, 1]))
# Output: [2, 4]

# Only max breaks
print(breaking_records([3, 4, 21, 36, 10, 28, 35, 5, 24, 42]))
# Output: [4, 0]

# No breaks
print(breaking_records([10, 10, 10, 10]))
# Output: [0, 0]

# Strictly increasing
print(breaking_records([1, 2, 3, 4, 5]))
# Output: [4, 0]

# Strictly decreasing
print(breaking_records([5, 4, 3, 2, 1]))
# Output: [0, 4]
```

## Testing

The solution includes comprehensive test coverage with 20 test cases.

### Test Coverage
- ✓ Edge cases (single game, all same scores, all zeros)
- ✓ Boundary conditions (strictly increasing/decreasing sequences)
- ✓ Mixed scenarios (alternating breaks, equal max/min breaks)
- ✓ Constraint adherence (values from 0 to 10^8, various array lengths)
- ✓ Tie handling (repeated values that don't break records)
- ✓ Long sequences (up to constraint limits)
- ✓ Large value differences

### Running Tests

**Full test suite:**
```bash
python test_breaking_records.py
```

### Test Results

All 20 tests pass with 100% success rate:
```
============================================================
Results: 20/20 tests passed
============================================================
```

## Files

- [**`breaking_records.py`**](breaking_records.py) - Main solution implementation
- [**`test_breaking_records.py`**](test_breaking_records.py) - Comprehensive test suite (20 tests)
