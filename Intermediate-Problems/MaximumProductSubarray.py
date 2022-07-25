#meh=maximum ending here
#mineh=minimum ending here
#msf=max so far
#Dynamic Programming
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        meh=mineh=msf=nums[0]
        n=len(nums)
        for i in range(1,n):
            temp=max(max(nums[i],nums[i]*meh),nums[i]*mineh)
            mineh=min(min(nums[i],nums[i]*meh),nums[i]*mineh)
            meh=temp
            msf=max(msf,meh)
        return msf
