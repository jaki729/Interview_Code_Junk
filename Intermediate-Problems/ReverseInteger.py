class Solution:
    def reverse(self, x: int) -> int:
        revdigit,x_remaining=0,abs(x)
        while(x_remaining):
            revdigit=revdigit*10+x_remaining%10
            x_remaining//=10
            if revdigit > 2147483647:
                return 0
        return -revdigit if x<0 else revdigit
