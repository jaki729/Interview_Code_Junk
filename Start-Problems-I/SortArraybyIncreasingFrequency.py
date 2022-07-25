from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        s=collections.Counter(nums)
        nums.sort(key=lambda x:(s[x],-x))
        return nums
