import itertools
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in itertools.combinations(range(len(nums)),2):
            if nums[i]+nums[j]==target:
                return i,j
        return None
