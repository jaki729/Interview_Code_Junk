'''
https://leetcode.com/problems/palindrome-number/description/

The time complexity of the optimized code is still O(log n), 
as we need to iterate through the digits of the input number to calculate its reverse.
'''
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        
        rev_digit, temp = 0, x
        while temp:
            rev_digit = rev_digit * 10 + temp % 10
            temp //= 10
        
        return rev_digit == x

