'''
Example 1:
Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Example 2:
Input: nums = [2,0,1]
Output: [0,1,2]
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        l, r = 0,len(nums)-1
        i=0

        def swap(i,j):
            temp=nums[i]
            nums[i]=nums[j]
            nums[j]=temp

        while i<=r:
            if nums[i]==0:
                swap(l,i)
                l+=1
            elif nums[i]==2:
                swap(i,r)
                r-=1
                i-=1
            i+=1
'''
The technique used is quick sort parition 
'''
