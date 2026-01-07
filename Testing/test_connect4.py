from Code.connect4 import calcPlayerPoints


def run_tests():
    """Run comprehensive test cases for calcPlayerPoints function."""
    tests = []
    
    tests.append({
        "name": "Test 1: Simple horizontal sequence of 4",
        "board": [
            "BBBB",
            "WWWW",
            "BWBW",
            "WBWB"
        ],
        "player": "B",
        "expected": 1
    })
    
    tests.append({
        "name": "Test 2: Simple horizontal sequence of 4 for W",
        "board": [
            "BBBB",
            "WWWW",
            "BWBW",
            "WBWB"
        ],
        "player": "W",
        "expected": 1
    })
    
    tests.append({
        "name": "Test 3: Vertical sequence of 5 for W",
        "board": [
            "BWWWW",
            "BWBWB",
            "BWBWB",
            "BWBWB",
            "BWBWB"
        ],
        "player": "W",
        "expected": 5
    })
    
    tests.append({
        "name": "Test 4: Diagonal sequence of 4 (down-right)",
        "board": [
            "BWWB",
            "WBWB",
            "WWBW",
            "BWWW"
        ],
        "player": "B",
        "expected": 0
    })
    
    tests.append({
        "name": "Test 5: Diagonal sequence of 4 (down-left) for W",
        "board": [
            "BWWB",
            "WWBW",
            "WBWB",
            "BWWW"
        ],
        "player": "W",
        "expected": 0
    })
    
    tests.append({
        "name": "Test 6: Multiple sequences for W",
        "board": [
            "BBBB",
            "WWWW",
            "BBBB",
            "WWWW"
        ],
        "player": "W",
        "expected": 2
    })
    
    tests.append({
        "name": "Test 7: Sequence of 6 for W",
        "board": [
            "BBBBBB",
            "WWWWWW",
            "BWBWBW",
            "WBWBWB",
            "BWBWBW",
            "WBWBWB"
        ],
        "player": "W",
        "expected": 9
    })
    
    tests.append({
        "name": "Test 8: Sequence of 5 horizontal for W",
        "board": [
            "BBBBBW",
            "WWWWWB",
            "BWBWBW",
            "WBWBWB",
            "BWBWBW",
            "WBWBWB"
        ],
        "player": "W",
        "expected": 9
    })
    
    tests.append({
        "name": "Test 9: No sequences of 4+ for W",
        "board": [
            "BBBW",
            "WWWB",
            "BWBW",
            "WBWB"
        ],
        "player": "W",
        "expected": 1
    })
    
    tests.append({
        "name": "Test 10: Multiple directions",
        "board": [
            "BBBBWW",
            "BWWWBW",
            "BWWBWW",
            "BWBWWW",
            "WWWWWB",
            "WWWWBB"
        ],
        "player": "B",
        "expected": 2
    })
    
    tests.append({
        "name": "Test 11: Large board with sequence of 7 for W",
        "board": [
            "BBBBBBBWWW",
            "WWWWWWWBBB",
            "BWBWBWBWBW",
            "WBWBWBWBWB",
            "BWBWBWBWBW",
            "WBWBWBWBWB",
            "BWBWBWBWBW",
            "WBWBWBWBWB",
            "BWBWBWBWBW",
            "WBWBWBWBWB"
        ],
        "player": "W",
        "expected": 46
    })
    
    tests.append({
        "name": "Test 12: Multiple diagonal sequences for W",
        "board": [
            "BWWWBW",
            "WBWWWB",
            "WWBWBW",
            "BWWBWW",
            "WBWWBW",
            "WBWWWB"
        ],
        "player": "W",
        "expected": 7
    })
    
    tests.append({
        "name": "Test 13: Vertical and horizontal combined",
        "board": [
            "BBBBWW",
            "BWWWBW",
            "BWWWBW",
            "BWWWBW",
            "WWWWWB",
            "WWWWBB"
        ],
        "player": "B",
        "expected": 2
    })
    
    tests.append({
        "name": "Test 14: Complex pattern with both players",
        "board": [
            "BBBBWW",
            "WWWWBB",
            "BBWWBW",
            "WWBBWB",
            "BWBWBW",
            "WBWBWB"
        ],
        "player": "B",
        "expected": 3
    })
    
    tests.append({
        "name": "Test 15: Large board with multiple sequences",
        "board": [
            "BBBBBWWW",
            "WWWWWBBB",
            "BWBWBWBW",
            "BWBWBWBW",
            "BWBWBWBW",
            "BWBWBWBW",
            "WWWWWBBB",
            "BBBWWWWW"
        ],
        "player": "B",
        "expected": 8
    })
    
    passed = 0
    failed = 0
    
    print("=" * 70)
    print("Running Connect 4 Tests")
    print("=" * 70)
    
    for i, test in enumerate(tests, 1):
        result = calcPlayerPoints(test["board"], test["player"])
        expected = test["expected"]
        
        if result == expected:
            passed += 1
            print(f"\n✓ {test['name']}")
            print(f"  Result: {result} (PASS)")
        else:
            failed += 1
            print(f"\n✗ {test['name']}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")
            print(f"  Difference: {result - expected}")
            print(f"  Board:")
            for row in test["board"]:
                print(f"    {row}")
            print(f"  Player: {test['player']}")
    
    print("\n" + "=" * 70)
    print(f"Test Results: {passed} passed, {failed} failed out of {len(tests)} total")
    print("=" * 70)
    
    return failed == 0


if __name__ == "__main__":
    all_passed = run_tests()
    exit(0 if all_passed else 1)
