#m1
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum=sum(nums)
        left_sum=0
        for i,num in enumerate(nums):
            total_sum-=num
            if left_sum==total_sum:
                return i
            left_sum+=num
        return -1
 #m2
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        mid=n//2
        left_sum=0
        right_sum=0
        for i in range(mid):
            left_sum+=nums[i]
        for i in range(n-1,mid,-1):
            right_sum+=nums[i]
        if right_sum>left_sum:
            while(right_sum>left_sum and mid<n-1):
                right_sum-=nums[mid]
                left_sum+=nums[mid-1]
                mid+=1
        else:
            while(left_sum>right_sum and mid>0):
                right_sum+=nums[mid]
                left_sum-+nums[mid-1]
                mid-=1
        if right_sum==left_sum:
          print("First Point of equilibrium is at index =" , mid);
        return;
    print("First Point of equilibrium is at index =" , -1);
