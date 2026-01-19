import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from Code.most_water import maxArea

def run_tests():
    test_cases = [
        ([1,8,6,2,5,4,8,3,7], 49, "Example case - optimal container"),
        ([1,1], 1, "Two lines of equal height"),
        ([4,3,2,1,4], 16, "Symmetric case"),
        ([1,2,1], 2, "Small array with peak in middle"),
        ([1,2,4,3], 4, "Increasing then decreasing"),
        ([2,3,10,5,7,8,9], 36, "Mixed heights with optimal at ends"),
        ([1,8,6,2,5,4,8,25,7], 49, "High peak in middle (not optimal)"),
        ([1,1,1,1,1], 4, "All equal heights"),
        ([5,4,3,2,1], 6, "Strictly decreasing"),
        ([1,2,3,4,5], 6, "Strictly increasing"),
        ([10,9,8,7,6,5,4,3,2,1], 25, "Long decreasing sequence"),
        ([1,2,3,4,5,6,7,8,9,10], 25, "Long increasing sequence"),
        ([100,1,1,1,1,1,1,1,1,100], 900, "High values at both ends"),
        ([1,100,100,1], 100, "High values in middle"),
        ([5,2,12,1,5,3,4,11,9,4], 55, "Complex case"),
        ([1,3,2,5,25,24,5], 24, "Peak near end"),
        ([3,9,3,4,7,2,12,6], 45, "Multiple local maxima"),
        ([10,10,10], 20, "Three equal heights"),
        ([1,1000000], 1, "Maximum height difference"),
        ([1000000,1000000], 1000000, "Two maximum heights"),
    ]
    
    failed_tests = []
    passed_tests = 0
    
    for i, (height, expected, description) in enumerate(test_cases, 1):
        result = maxArea(height)
        if result == expected:
            passed_tests += 1
            print(f"PASS Test {i}: {description}")
            print(f"  Height: {height}")
            print(f"  Result: {result} (Expected: {expected})")
        else:
            failed_tests.append((i, height, expected, result, description))
            print(f"FAIL Test {i}: {description}")
            print(f"  Height: {height}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
            print(f"  DIFFERENCE: Expected {expected}, but got {result}")
    
    print(f"\n{'='*60}")
    print(f"Results: {passed_tests}/{len(test_cases)} tests passed")
    
    if failed_tests:
        print(f"\n{'='*60}")
        print("FAILED TESTS SUMMARY:")
        for test_num, height, expected, result, description in failed_tests:
            print(f"  Test {test_num}: {description}")
            print(f"    Height: {height}")
            print(f"    Expected: {expected}")
            print(f"    Got: {result}")
            print()
    
    return len(failed_tests) == 0

if __name__ == "__main__":
    all_passed = run_tests()
    exit(0 if all_passed else 1)
