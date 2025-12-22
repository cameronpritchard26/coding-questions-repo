def isAdditiveNumber(num):
    """
    Check if a number is additive.
    
    An additive number is one whose digits can be partitioned to form an additive sequence.
    A valid additive sequence should contain at least three numbers, and each subsequent 
    number must equal the sum of the previous two numbers.
    
    Args:
        num: An integer or string representing the number to check
    
    Returns:
        True if the number is additive, False otherwise
    """
    s = str(num)
    n = len(s)
    
    if n < 3:
        return False
    
    for i in range(1, n):
        for j in range(i + 1, n):
            if is_valid_sequence(s, 0, i, j):
                return True
    
    return False


def is_valid_sequence(s, start1, start2, start3):
    """
    Check if the string can form a valid additive sequence starting with
    the first number from [start1:start2) and second number from [start2:start3).
    """
    if s[start1] == '0' and start2 - start1 > 1:
        return False
    if s[start2] == '0' and start3 - start2 > 1:
        return False
    
    num1 = int(s[start1:start2])
    num2 = int(s[start2:start3])
    
    pos = start3
    
    while pos < len(s):
        num3 = num1 + num2
        num3_str = str(num3)
        
        if not s[pos:].startswith(num3_str):
            return False
        
        pos += len(num3_str)
        num1 = num2
        num2 = num3
    
    return True
