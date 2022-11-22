'''
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and uses only constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2

Example 2:
Input: nums = [3,1,3,4,2]
Output: 3
This problem can be solved by identifying Linked List cycle of the inedxes as nodes and solving it using Floyd's Cycle Detection algorithm
math behind the cycle detection
2*slow_ptr=fast_ptr
=>2*(p+c-x)=p+c-x+c=p+2c-x
=>p-x=0
'''
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # taking two ptrs
        slow,fast=0,0 # 0 is not the part of the cycle
        while True: # until they intersect at the begining
            slow=nums[slow] # whatever it is going to point at
            fast=nums[nums[fast]] # using the equation 2*slow_ptr=fast_ptr
            if slow == fast:
                break
            
        #2nd phase of cycle
        slow2=0 # keep incrementing this until they intersect on 2nd round
        while True:
            slow=nums[slow]
            slow2=nums[slow2]
            if slow == slow2: # until they intersect
                return slow
