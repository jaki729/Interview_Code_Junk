'''
Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

we start from the start point 
we try to merge the overlapping intervals from the start to end point of the interval
tc=O(nlog n) n=no. of intervals given
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key = lambda i : i[0]) #sort by start
        ans=[intervals[0]] #to avoid edge cases

        for start,end in intervals[1:]: #taking the end value
            last_end=ans[-1][1] # getting the end value of most recent interval
            if start <= last_end: # if overlapping
                ans[-1][1] = max(last_end, end) # we merge the intervals
            else:
                # if non overlapping simply append to the list
                ans.append([start,end])
        return ans
