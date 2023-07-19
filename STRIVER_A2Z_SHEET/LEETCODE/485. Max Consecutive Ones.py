'''
https://leetcode.com/problems/max-consecutive-ones/description/
TC=O(n)
SC=(1)
'''
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Initialize the current count of consecutive 1s and the maximum count.
        count = 0
        max_c = 0

        # Iterate over the list of integers.
        for i in range(len(nums)):
            # If the current integer is 1, increment the count.
            if nums[i] == 1:
                count += 1

            # Otherwise, reset the count to 0.
            else:
                count = 0

            # Update the maximum count.
            max_c = max(max_c, count)

        # Return the maximum count.
        return max_c
