'''
https://leetcode.com/problems/move-zeroes/description/
TC=O(n)
SC=O(1)
'''
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # Initialize two pointers, one for iterating the array (i) and one for placing non-zero elements (nonZeroIndex)
        nonZeroIndex = 0
        
        # Iterate through the array using pointer i
        for i in range(len(nums)):
            # If the current element is non-zero
            if nums[i] != 0:
                # Place the non-zero element at the nonZeroIndex
                nums[nonZeroIndex] = nums[i]
                # Increment the nonZeroIndex to prepare for the next non-zero element
                nonZeroIndex += 1
        
        # Fill the remaining elements from nonZeroIndex to the end of the array with zeroes
        while nonZeroIndex < len(nums):
            nums[nonZeroIndex] = 0
            nonZeroIndex += 1
