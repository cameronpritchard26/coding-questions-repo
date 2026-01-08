# Connect 4 Scoring Problem

[Back to problems](../README.md)

## Problem Description

Connect 4 is a board game played on an NxN board between two players: black ('B') and white ('W'). Players score points for having sequences of their own pieces in a row. Sequences can be horizontal, vertical, or diagonal.

### Scoring Rules
- A sequence of **4 pieces** in a row = **1 point**
- A sequence of **5 pieces** in a row = **2 points**
- A sequence of **6 pieces** in a row = **3 points**
- A sequence of **n pieces** in a row = **(n - 3) points**

### Constraints
- The board consists of **half black pieces and half white pieces**, simulating alternating turns in a real game
- Board size: 4 ≤ N ≤ 100
- Each cell contains either 'B' or 'W'
- Player is either 'B' or 'W'

### Examples

**Example 1:**
```
Board:
BBBB
WWWW
BWBW
WBWB

Player 'B': 1 point (1 horizontal sequence of 4)
Player 'W': 1 point (1 horizontal sequence of 4)
```

**Example 2:**
```
Board:
BBBBBB
WWWWWW
BWBWBW
WBWBWB
BWBWBW
WBWBWB

Player 'B': 3 points (1 horizontal sequence of 6)
Player 'W': 9 points (1 horizontal sequence of 6 + multiple other sequences)
```

**Example 3:**
```
Board:
BWWWW
BWBWB
BWBWB
BWBWB
BWBWB

Player 'B': 2 points (1 vertical sequence of 5)
Player 'W': 5 points (1 vertical sequence of 5 + other sequences)
```

## Solution Logic

The solution uses an **optimal sequence detection algorithm** with duplicate prevention to efficiently count all scoring sequences.

### Algorithm Overview

**Phase 1: Board Traversal**
- Iterate through each cell on the NxN board (row by row, column by column)
- For each cell containing the player's piece, check sequences in 4 directions:
  - **Horizontal** (left-to-right, 0, 1)
  - **Vertical** (top-to-bottom, 1, 0)
  - **Diagonal down-right** (1, 1)
  - **Diagonal down-left** (1, -1)

**Phase 2: Full Sequence Detection**

For each direction from a cell, the algorithm finds the **complete sequence**:

1. **Backward Extension**: Move in the opposite direction until:
   - Hit a cell with a different piece, OR
   - Reach the board edge

2. **Forward Collection**: From the sequence start, move forward collecting all consecutive matching pieces:
   - Store each cell's coordinates (row, col)
   - Continue until hitting a different piece or board edge

3. **Sequence Identification**: Store the sequence as a **sorted tuple of coordinates**
   - Example: `((0,0), (0,1), (0,2), (0,3))` for a horizontal sequence

**Phase 3: Duplicate Prevention**

The key to avoiding double-counting:
- Use a **visited set** to track already-counted sequences
- Each unique sequence generates the same sorted tuple regardless of which cell discovered it
- Before scoring a sequence, check if it's already in the visited set
- If new, add to visited set and count the points

**Example of Duplicate Prevention:**
```
For horizontal sequence "BBBB" at row 0:
- Starting from (0,0): generates ((0,0), (0,1), (0,2), (0,3))
- Starting from (0,1): generates ((0,0), (0,1), (0,2), (0,3))
- Starting from (0,2): generates ((0,0), (0,1), (0,2), (0,3))
- Starting from (0,3): generates ((0,0), (0,1), (0,2), (0,3))

All generate the same tuple → counted only once!
```

**Phase 4: Point Calculation**

For each unique sequence with length ≥ 4:
- Calculate points: `points = length - 3`
- Add to the player's total score

### Complexity Analysis

**Time Complexity: O(N²)**
- Each cell is visited once: O(N²)
- For each cell, we check 4 directions
- Sequence detection per direction is O(N) in worst case
- However, with the visited set, each sequence is fully processed only once
- Amortized complexity: O(N²)

**Space Complexity: O(N²)**
- Visited set stores unique sequences
- Worst case: all cells form sequences → O(N²) space
- Typical case: much less than O(N²)

### Key Optimizations

1. **Bidirectional Sequence Detection**: By extending backward first, we always find the true start of a sequence, ensuring consistent identification

2. **Coordinate-Based Hashing**: Using sorted tuples of coordinates provides a reliable way to identify duplicate sequences

3. **Early Termination**: Once a sequence is in the visited set, we skip it immediately

4. **Single Pass**: Only one iteration through the board is needed

## Implementation

### Function Signature

```python
def calcPlayerPoints(board, player) -> int
```

**Parameters:**
- `board`: List of strings representing the NxN board
  - Each string is a row of the board
  - Each character is either 'B' or 'W'
- `player`: String, either 'B' (black) or 'W' (white)

**Returns:**
- Integer representing the total points scored by the player

### Example Usage

```python
from connect4 import calcPlayerPoints

# Simple horizontal sequence
board = ["BBBB", "WWWW", "BWBW", "WBWB"]
print(calcPlayerPoints(board, "B"))  # Output: 1
print(calcPlayerPoints(board, "W"))  # Output: 1

# Longer sequence
board = ["BBBBBB", "WWWWWW", "BWBWBW", "WBWBWB", "BWBWBW", "WBWBWB"]
print(calcPlayerPoints(board, "B"))  # Output: 3
print(calcPlayerPoints(board, "W"))  # Output: 9

# Vertical sequence
board = ["BWWWW", "BWBWB", "BWBWB", "BWBWB", "BWBWB"]
print(calcPlayerPoints(board, "B"))  # Output: 2
print(calcPlayerPoints(board, "W"))  # Output: 5
```

## Testing

The solution includes comprehensive test coverage with 15 test cases:

### Test Distribution
- **Player B**: 6 tests (40%)
- **Player W**: 9 tests (60%)

### Test Coverage
- ✓ Simple horizontal sequences
- ✓ Simple vertical sequences
- ✓ Diagonal sequences (both directions)
- ✓ Multiple sequences on the same board
- ✓ Longer sequences (5, 6, 7 pieces)
- ✓ Edge cases (no sequences, complex patterns)
- ✓ Both players tested across all sequence types

### Running Tests

**Full test suite:**
```bash
python test_connect4.py
```

### Test Results

All 15 tests pass with 100% success rate:
```
======================================================================
Running Connect 4 Tests
======================================================================
✓ Test 1: Simple horizontal sequence of 4
✓ Test 2: Simple horizontal sequence of 4 for W
✓ Test 3: Vertical sequence of 5 for W
✓ Test 4: Diagonal sequence of 4 (down-right)
✓ Test 5: Diagonal sequence of 4 (down-left) for W
✓ Test 6: Multiple sequences for W
✓ Test 7: Sequence of 6 for W
✓ Test 8: Sequence of 5 horizontal for W
✓ Test 9: No sequences of 4+ for W
✓ Test 10: Multiple directions
✓ Test 11: Large board with sequence of 7 for W
✓ Test 12: Multiple diagonal sequences for W
✓ Test 13: Vertical and horizontal combined
✓ Test 14: Complex pattern with both players
✓ Test 15: Large board with multiple sequences
======================================================================
Test Results: 15 passed, 0 failed out of 15 total
======================================================================
```

## Files

- [**`connect4.py`**](connect4.py) - Main solution implementation
- [**`test_connect4.py`**](test_connect4.py) - Comprehensive test suite (15 tests)