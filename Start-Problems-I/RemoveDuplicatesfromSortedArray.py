#m1
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        write_index=1
        for i in range(1,len(nums)):
            if nums[write_index-1] != nums[i]:
                nums[write_index]=nums[i]
                write_index+=1
        return write_index
#m2
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0 or n==1:
            return n
        j=0
        for i in range(0,n-1):
            if nums[i]!=nums[i+1]:
                nums[j]=nums[i]
                j+=1
        nums[j]=nums[n-1]
        j+=1
        return j
