#m1
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
#m2
class Solution:
    def myPow(self, x: float, n: int) -> float:
        result,power=1,n
        if n<0:
            power,x=-power,1/x
        while power:
            if power & 1:
                result*=x
            x,power=x*x,power>>1
        return result
