#m1
class Solution:
    def mySqrt(self, x: int) -> int:
        ans = x
        while not ans * ans - x < 1:
            ans = (ans + x / ans) / 2
        return int(ans)
#m2
class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0,  x
        while left <= right:
            mid = left + (right - left) // 2
            if mid * mid > x:
                right = mid - 1
            elif mid * mid < x:
                left = mid + 1
            else:
                return mid
        # left > right
        return right
