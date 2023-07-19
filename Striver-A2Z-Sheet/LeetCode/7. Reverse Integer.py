'''
https://leetcode.com/problems/reverse-integer/description/

The time complexity of the solution is O(log10(x)).
'''
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0 :
            sign = -1
            x = -x
        else:
            sign = 1
        rev_digit = 0
        while x > 0:
            rev_digit = rev_digit * 10 + x % 10
            x //= 10
        if rev_digit > 2147483647:
            return 0
        return sign * rev_digit
