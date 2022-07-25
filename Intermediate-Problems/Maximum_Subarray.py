#msf=maximum so far
#meh=maximum ending here
#curr_max=current maximum
#Dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size=len(nums)
        msf=nums[0]
        curr_max=nums[0]
        for i in range(1,size):
            curr_max=max(nums[i],curr_max+nums[i])
            msf=max(msf,curr_max)
        return msf
#Greedy
from sys import maxsize
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        msf=-maxsize-1
        meh=0
        start=0
        end=0
        s=0
        size=len(nums)
        for i in range(0,size):
            meh+=nums[i]
            if msf<meh:
                msf=meh
                start=s
                end=i
            if meh<0:
                meh=0
                s=i+1
        return msf
