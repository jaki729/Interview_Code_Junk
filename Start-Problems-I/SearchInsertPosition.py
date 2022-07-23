#m1
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        result=0
        if len(nums)==1 and target>nums[0]:
            return 1
        for i in range(len(nums)-1):
            if target == nums[i]:
                result=i
                return result
                break
            elif target>nums[i] and target<=nums[i+1]:
                result=i+1
                return result
                break
            elif target>nums[i+1] and (len(nums)-1) == i+1:
                result=len(nums)
                return result
                break
            elif target<nums[i] and i==0:
                result=0
                return result
                break
            elif target>nums[i] and target>nums[i+1]:
                continue
        return result
      
#m2
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        while l<=r:
            m=(l+r)//2
            if target==nums[m]:
                return m
            if target>nums[m]:
                l=m+1
            else:
                r=m-1
        return l
