class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        min_num = -2**31
        max_num = 2**31 - 1
        result = abs(dividend) // abs(divisor)
        if (dividend > 0 and divisor > 0) or (dividend < 0 and divisor < 0):
            return min(result, max_num)
        else:
             return max(-result, min_num)
