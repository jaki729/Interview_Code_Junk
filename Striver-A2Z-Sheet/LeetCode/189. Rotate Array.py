'''
https://leetcode.com/problems/rotate-array/description/
TC=O(N)
SC=O(1)
'''
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # Calculate the effective number of rotations by taking modulo with the length of the array
        n = k % len(nums)
        
        # Perform the rotation by assigning the concatenated slices of the array to the original array
        nums[:] = nums[-n:] + nums[:-n]
        
        # Return the rotated array
        return nums
