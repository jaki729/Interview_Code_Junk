class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num ==1:
            return True
        if num ==2:
            return False
        start =2
        end = num
        while start<=end:
            mid = (start+end) //2
            if mid*mid == num:
                return True
            elif mid*mid > num:
                end = mid -1
            else:
                start = mid +1    
        return False
