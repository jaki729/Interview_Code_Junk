#msf=maximum so far
#meh=maximum ending here
#curr_max=current maximum
#Dynamic programming
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSubArr=nums[0]
        current_sum=0
        for i in nums:
            if current_sum<0:
                current_sum=0
            current_sum+=i
            maxSubArr=max(maxSubArr,current_sum)
        return maxSubArr
    
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
