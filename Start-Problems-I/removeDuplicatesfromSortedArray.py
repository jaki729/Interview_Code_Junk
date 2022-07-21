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
