class Solution:
def searchRange(self, nums: List[int], target: int) -> List[int]:
    left=self.first(nums,target)
    right=self.last(nums,target)
    return [left,right]

def first(self,arr, x):
    n=len(arr)
    low = 0
    high = n - 1
    res = -1
    while (low <= high):
        mid = (low + high) // 2        
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1           
        else:
            res = mid
            high = mid - 1 
    return res
def last(self,arr, x):    
    n=len(arr)
    low = 0
    high = n - 1
    res = -1 
    while(low <= high):
        mid = (low + high) // 2        
        if arr[mid] > x:
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            res = mid
            low = mid + 1 
    return res
