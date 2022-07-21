class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        else:
            return self.reverseInteger(x)==x
    
    def reverseInteger(self,x):
        r=0
        while x:
            d=x%10
            r=r*10+d
            x//=10
        return r
