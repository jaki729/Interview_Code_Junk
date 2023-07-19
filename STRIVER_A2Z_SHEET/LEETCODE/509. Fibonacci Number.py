'''
https://leetcode.com/problems/fibonacci-number/description/

 This approach has a time complexity of O(n) and a space complexity of O(1).
'''
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b
