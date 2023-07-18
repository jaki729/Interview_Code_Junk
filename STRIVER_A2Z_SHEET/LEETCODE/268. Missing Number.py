'''
https://leetcode.com/problems/missing-number/description/
time complexity is O(n).
 space complexity is O(1)
 '''
class Solution:
    def missingNumber(self, arr: List[int]) -> int:
        length = len(arr)  # Get the length of the array
        summation = (length * (length + 1)) // 2  # Calculate the expected sum using the formula for the sum of a series
        return summation - sum(arr)  # Subtract the actual sum of the array from the expected sum to find the missing number
