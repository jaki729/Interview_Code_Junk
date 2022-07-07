#Jump Game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        further_reach_so_far,last_index=0,len(nums)-1
        i=0
        while i<=further_reach_so_far and further_reach_so_far<last_index:
            further_reach_so_far=max(further_reach_so_far,nums[i]+i)
            i+=1
        return further_reach_so_far>=last_index
