class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates=set()
        visited=set()
        for i in nums:
            if i in visited:
                duplicates.add(i)
            visited.add(i)
        return duplicates
