class Solution:
    def computeParity(self, n):
        n^=n>>32
        n^=n>>16
        n^=n>>8
        n^=n>>4
        n^=n>>2
        n^=n>>1
        if (n&1)==1:
            return "odd"
        else:
            return "even"
