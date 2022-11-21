#https://leetcode.com/problems/maximum-subarray/
'''
Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Example 2:
Input: nums = [1]
Output: 1

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub=nums[0]
        cur_sum=0
        for i in nums:
            if cur_sum<0:
                cur_sum=0
            cur_sum+=i
            max_sub=max(max_sub,cur_sum)
        return max_sub
'''
The above technique used is sliding window protocol which gives an effeciency of O(n)
OR
The other technique used can be using 3 for loops(cubic solution) and 2 loops(quadratic solution) and storing the current sum of the sub array.
'''
