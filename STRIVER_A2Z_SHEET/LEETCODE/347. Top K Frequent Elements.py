'''
https://leetcode.com/problems/top-k-frequent-elements/
method tc = O(n)

hashmap = {}: Create an empty dictionary to store the frequency count of each element in the array.
freq = [[] for i in range(len(nums) + 1)]: Create an empty list of lists (buckets) to store elements with the same frequency.
for n in nums: hashmap[n] = 1 + hashmap.get(n,0): Traverse the array and increment the frequency count of each element in the dictionary.
for n,c in hashmap.items(): freq[c].append(n): Traverse the dictionary and add each element to the bucket corresponding to its frequency.
ans = []: Create an empty list to store the k most frequent elements.
for i in range(len(freq) - 1, 0, -1):: Iterate through the buckets from highest to lowest frequency.
for n in freq[i]: ans.append(n): Add each element in the bucket to the result list.
if len(ans) == k: return ans: If k elements have been added to the result list, return it.
 '''
# Method  (hashing using bucket sort)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        freq = [ [] for i in range(len(nums) + 1)]
        for n in nums:
            hashmap[n] = 1 + hashmap.get(n,0)
        for n,c in hashmap.items():
            freq[c].append(n)
        ans = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                ans.append(n)
                if len(ans) == k:
                    return ans
