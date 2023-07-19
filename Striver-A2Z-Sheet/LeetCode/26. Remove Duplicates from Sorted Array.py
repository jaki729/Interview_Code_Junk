'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/
TC=O(n)
SC=O(1)
'''
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        
        # If the array has 0 or 1 element, no duplicates to remove
        if n == 0 or n == 1:
            return n
        
        j = 0  # Initialize a pointer j to keep track of the position to update
        
        # Iterate over the array from index 0 to n-2
        for i in range(0, n-1):
            # If the current element is not equal to the next element, it's not a duplicate
            if nums[i] != nums[i+1]:
                # Update the element at position j with the non-duplicate element
                nums[j] = nums[i]
                j += 1
        
        # Update the last element at position j with the last element of the original array
        nums[j] = nums[n-1]
        j += 1
        
        return j

#method 2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:
        nums[:]= sorted(set(nums))
        return len(nums)
