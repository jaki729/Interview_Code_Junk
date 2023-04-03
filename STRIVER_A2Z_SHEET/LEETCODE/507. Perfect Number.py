'''
https://leetcode.com/problems/perfect-number/
The time complexity of this code is O(sqrt(num)). 
This is because the loop runs from 2 to sqrt(num) and 
performs a constant number of operations in each iteration. 
The space complexity is O(1), as the amount of memory used by the code is constant regardless of the input size.
'''
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num <= 1:
            return False
        divisors_sum = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                divisors_sum += i
                if i != num / i:
                    divisors_sum += num / i
        
        return divisors_sum == num
