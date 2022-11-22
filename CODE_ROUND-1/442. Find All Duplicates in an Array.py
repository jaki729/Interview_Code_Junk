'''
Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer appears once or twice, return an array of all the integers that appears twice.
You must write an algorithm that runs in O(n) time and uses only constant extra space.
Example 1:
Input: nums = [4,3,2,7,8,2,3,1]
Output: [2,3]

Example 2:
Input: nums = [1,1,2]
Output: [1]

Example 3:
Input: nums = [1]
Output: []

Not much difference in time complexity of the 2 solutions.
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res=[] # store the duplicate number
        for number in nums: # iterate through the nums
            number=abs(number) 

            if nums[number-1] > 0: # if the number present in index is not visited 
                nums[number - 1] *= -1 # if the number is visited atleast once then we multiply with -1
            else:
                res.append(number) 
        return res
      
# OR

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates=set()
        visited=set()
        for i in nums:
            if i in visited:
                duplicates.add(i)
            visited.add(i)
        return duplicates
