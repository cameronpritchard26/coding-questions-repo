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
```

### Connect 4 Scoring

**File:** `connect4.py`

#### Problem Description

Connect 4 is a board game played on an NxN board between two players: black ('B') and white ('W'). Players score points for having sequences of their own pieces in a row. Sequences can be horizontal, vertical, or diagonal.

**Scoring Rules:**
- A sequence of **4 pieces** in a row = **1 point**
- A sequence of **5 pieces** in a row = **2 points**
- A sequence of **6 pieces** in a row = **3 points**
- A sequence of **n pieces** in a row = **(n - 3) points**

**Constraints:**
- The board consists of **half black pieces and half white pieces**, simulating alternating turns
- Board size: 4 ≤ N ≤ 100
- Each cell contains either 'B' or 'W'

**Examples:**

Board:
```
BBBB
WWWW
BWBW
WBWB
```
- Player 'B': 1 point (1 horizontal sequence of 4)
- Player 'W': 1 point (1 horizontal sequence of 4)

#### Solution Logic

The solution uses an **optimal sequence detection algorithm** with duplicate prevention:

**Phase 1: Board Traversal**
- Iterate through each cell on the NxN board
- For each cell containing the player's piece, check sequences in 4 directions:
  - Horizontal (left-to-right)
  - Vertical (top-to-bottom)
  - Diagonal down-right
  - Diagonal down-left

**Phase 2: Full Sequence Detection**
- For each direction, find the **complete sequence** by:
  1. Moving backward (opposite direction) until hitting a different piece or board edge
  2. Moving forward from the start to collect all consecutive matching pieces
  3. Storing the sequence as a sorted tuple of coordinates

**Phase 3: Duplicate Prevention**
- Use a visited set to track already-counted sequences
- Each unique sequence (regardless of which cell discovered it) is counted exactly once
- The sorted tuple ensures the same sequence always generates the same identifier

**Phase 4: Point Calculation**
- For sequences with length ≥ 4:
  - Calculate points as `(length - 3)`
  - Add to the player's total score

**Algorithm Complexity:**
- **Time:** O(N²) where N is the board dimension
- **Space:** O(N²) for the visited set in worst case

**Key Optimization:**
The algorithm avoids counting the same sequence multiple times by finding the full extent of each sequence and using coordinate-based hashing to identify duplicates.

#### Function Signature

```python
def calcPlayerPoints(board, player) -> int
```

**Parameters:**
- `board`: List of strings representing the NxN board
- `player`: Either 'B' (black) or 'W' (white)

**Returns:**
- Integer representing the total points scored by the player

**Example Usage:**
```python
>>> board = ["BBBB", "WWWW", "BWBW", "WBWB"]
>>> calcPlayerPoints(board, "B")
1

>>> calcPlayerPoints(board, "W")
1

>>> board = ["BBBBBB", "WWWWWW", "BWBWBW", "WBWBWB", "BWBWBW", "WBWBWB"]
>>> calcPlayerPoints(board, "B")
3

>>> calcPlayerPoints(board, "W")
9
```

#### Testing

The solution includes comprehensive test coverage:
- **15 test cases** covering all sequence types and edge cases
- **60% test player 'W'**, 40% test player 'B'
- All tests pass with 100% success rate

Run tests:
```bash
python test_connect4.py
```

See `README_CONNECT4.md` for detailed documentation