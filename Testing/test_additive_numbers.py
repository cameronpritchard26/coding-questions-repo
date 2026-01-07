from ..Code.additive_numbers import isAdditiveNumber

def run_tests():
    test_cases = [
        (112, True, "1+1=2"),
        (1123, True, "1+1=2, 1+2=3"),
        (125, False, "1+2!=5"),
        (199100199, True, "1+99=100, 99+100=199"),
        (123, True, "1+2=3"),
        (1235, True, "1+2=3, 2+3=5"),
        (12012, True, "1+2=3 doesn't work, but 12+0=12"),
        (101, True, "1+0=1"),
        (1, False, "too short"),
        (12, False, "too short"),
        (0, False, "too short"),
        (199111, False, "no valid partition"),
        (198, False, "no valid partition"),
        (11, False, "too short"),
        (111, False, "no valid partition"),
        (235, True, "2+3=5"),
        (1212, False, "no valid partition"),
        (358, True, "3+5=8"),
        (112358, True, "1+1=2, 1+2=3, 2+3=5, 3+5=8"),
        (199100, True, "1+99=100"),
        (19910011, False, "no valid partition"),
        (12122436, True, "12+12=24, 12+24=36"),
        ("000", True, "0+0=0"),
        (101, True, "1+0=1"),
        (10, False, "too short"),
    ]
    
    failed_tests = []
    passed_tests = 0
    
    for i, (num, expected, description) in enumerate(test_cases, 1):
        result = isAdditiveNumber(num)
        if result == expected:
            passed_tests += 1
            print(f"PASS Test {i}: {num} -> {result} (Expected: {expected}) - {description}")
        else:
            failed_tests.append((i, num, expected, result, description))
            print(f"FAIL Test {i}: {num} -> {result} (Expected: {expected}) - {description}")
            print(f"  DIFFERENCE: Expected {expected}, but got {result}")
    
    print(f"\n{'='*60}")
    print(f"Results: {passed_tests}/{len(test_cases)} tests passed")
    
    if failed_tests:
        print(f"\n{'='*60}")
        print("FAILED TESTS SUMMARY:")
        for test_num, num, expected, result, description in failed_tests:
            print(f"  Test {test_num}: {num}")
            print(f"    Expected: {expected}")
            print(f"    Got: {result}")
            print(f"    Description: {description}")
            print()
    
    return len(failed_tests) == 0

if __name__ == "__main__":
    all_passed = run_tests()
    exit(0 if all_passed else 1)
