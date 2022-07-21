'''
Given an integer array nums, move all the even integers at the beginning of the array followed
by all the odd integers.Return any array that satisfies this condition.
'''

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        next_even,next_odd=0,len(nums)-1
        while next_even<next_odd:
            if nums[next_even]%2==0:
                next_even+=1
            else:
                nums[next_even],nums[next_odd]=nums[next_odd],nums[next_even]
                next_odd-=1
        return nums
