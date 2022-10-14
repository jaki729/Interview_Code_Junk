#m1
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i,n in enumerate(nums):
            difference =target-n
            if difference in hashmap:
                return [hashmap[difference],i]
            hashmap[n]=i
        return

#m2
import itertools
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,j in itertools.combinations(range(len(nums)),2):
            if nums[i]+nums[j]==target:
                return i,j
        return None
