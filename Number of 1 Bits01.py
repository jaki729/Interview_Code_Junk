class Solution:
    def hammingWeight(self, n: int) -> int:
        Bitsettable=[0]*256
        Bitsettable[0]=0
        for i in range(256):
            Bitsettable[i]=(i&1)+Bitsettable[i//2]
        return (Bitsettable[n & 0xff]+
                Bitsettable[(n>>8) & 0xff]+
                Bitsettable[(n>>16) & 0xff]+
                Bitsettable[(n>>24) & 0xff])
