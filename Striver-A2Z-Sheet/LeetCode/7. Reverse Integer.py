'''
https://leetcode.com/problems/reverse-integer/description/

The time complexity of the solution is O(log10(x)).
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
            x = -x  # Make x positive for reverse calculation
        else:
            sign = 1
        
        rev_digit = 0  # Initialize the reversed number
        
        while x > 0:
            # Extract the last digit of x and add it to the reversed number
            rev_digit = rev_digit * 10 + x % 10
            x //= 10  # Move to the next digit
        
        if rev_digit > 2147483647:  # Check for integer overflow
            return 0  # Return 0 if overflow occurs
        
        return sign * rev_digit  # Return the reversed number with the original sign

