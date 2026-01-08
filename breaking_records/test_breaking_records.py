from breaking_records import breaking_records

def run_tests():
    test_cases = [
        ([10, 5, 20, 20, 4, 5, 2, 25, 1], [2, 4], "Example with multiple breaks"),
        ([3, 4, 21, 36, 10, 28, 35, 5, 24, 42], [4, 0], "Only max breaks, no min breaks"),
        ([10], [0, 0], "Single game - no records broken"),
        ([10, 10, 10, 10], [0, 0], "All same scores - no records broken"),
        ([1, 2, 3, 4, 5], [4, 0], "Strictly increasing - only max breaks"),
        ([5, 4, 3, 2, 1], [0, 4], "Strictly decreasing - only min breaks"),
        ([100, 50, 150, 25, 200], [2, 2], "Alternating max and min breaks"),
        ([0, 0, 0], [0, 0], "All zeros - edge case with minimum value"),
        ([100000000, 0, 100000000], [0, 1], "Max constraint value (10^8)"),
        ([50, 100, 25, 150, 10, 200, 5], [3, 3], "Equal max and min breaks"),
        ([10, 20, 30, 25, 35], [3, 0], "Multiple max breaks, no min"),
        ([30, 20, 10, 15, 5], [0, 3], "Multiple min breaks, no max"),
        ([5, 10, 3, 15, 2, 20, 1], [3, 3], "Alternating pattern"),
        ([42, 42, 42, 43], [1, 0], "Repeated values then increase"),
        ([42, 42, 42, 41], [0, 1], "Repeated values then decrease"),
        ([1, 1000000, 1, 10000000, 1, 100000000], [3, 0], "Large value differences"),
        ([10, 5, 20], [1, 1], "Simple case with one of each"),
        ([100, 100, 101, 100, 99], [1, 1], "Ties don't break records"),
        ([7, 8, 9, 10, 11, 12, 13, 14, 15], [8, 0], "Long increasing sequence"),
        ([20, 19, 18, 17, 16, 15, 14, 13], [0, 7], "Long decreasing sequence"),
    ]
    
    failed_tests = []
    passed_tests = 0
    
    for i, (scores, expected, description) in enumerate(test_cases, 1):
        result = breaking_records(scores)
        if result == expected:
            passed_tests += 1
            print(f"PASS Test {i}: {description}")
            print(f"  Scores: {scores}")
            print(f"  Result: {result} (Expected: {expected})")
        else:
            failed_tests.append((i, scores, expected, result, description))
            print(f"FAIL Test {i}: {description}")
            print(f"  Scores: {scores}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            print(f"  DIFFERENCE: Expected {expected}, but got {result}")
    
    print(f"\n{'='*60}")
    print(f"Results: {passed_tests}/{len(test_cases)} tests passed")
    
    if failed_tests:
        print(f"\n{'='*60}")
        print("FAILED TESTS SUMMARY:")
        for test_num, scores, expected, result, description in failed_tests:
            print(f"  Test {test_num}: {description}")
            print(f"    Scores: {scores}")
            print(f"    Expected: {expected}")
            print(f"    Got: {result}")
            print()
    
    return len(failed_tests) == 0

if __name__ == "__main__":
    all_passed = run_tests()
    exit(0 if all_passed else 1)
