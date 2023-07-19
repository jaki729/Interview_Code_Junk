'''
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
TC=O(n)
SC=O(1)
'''
class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        rotates = 0
        
        # Step 1: Iterate over the array 'nums' from index 0 to n-1
        for i in range(n):
            # Step 2: Check if the current element is less than the previous element
            if nums[i] < nums[i-1]:
                rotates += 1
        
        # Step 3: Return True if the number of rotations is less than or equal to 1, otherwise False
        return True if rotates <= 1 else False
