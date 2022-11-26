'''
Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).
Example 1:
Input: x = 2.00000, n = 10
Output: 1024.00000

Example 2:
Input: x = 2.10000, n = 3
Output: 9.26100

Example 3:
Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
TC=O(log n)
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def evaluate(x,n):
            if x==0:
                return 0
            if n==0:
                return 1
            ans=evaluate(x * x , n//2)
            return x * ans if n%2 else ans
        ans=evaluate(x , abs(n))
        return ans if n>=0 else 1/ans
