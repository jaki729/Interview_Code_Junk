'''
Example 1:
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Example 2:
Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ans=len(nums)
        for i in range(len(nums)):
            ans+=(i-nums[i])
        return ans
'''
The above technique used is sum[array1]-sum[array2]=results in missing number.
OR
This problem can be done using xor operation=n1^n2
xor =>
1^1=0
0^0=0
1^0=1
0^1=1
'''