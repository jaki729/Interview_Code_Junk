class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        index=[]
        for i,j in enumerate(nums):
            if j==target:
                index.append(i)
        return index
