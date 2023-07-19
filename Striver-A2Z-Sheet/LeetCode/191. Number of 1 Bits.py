'''
https://leetcode.com/problems/number-of-1-bits/description/
The code defines a class Solution with a method hammingWeight 
that takes an integer n as input and returns an integer representing the number of bits set to 1 in the binary representation of n.
It initializes a variable c to keep track of the count of bits set to 1.
The code enters a loop that iterates 31 times. 
This is because integers in Python are typically represented using 32 bits, and we are considering only the first 31 bits (from 0 to 30).
Inside the loop, the code checks each bit of n starting from the least significant bit (bit 0) up to the most significant bit (bit 30).
To check a specific bit, it performs a bitwise right shift of n by i positions (n >> i). This moves the bit that needs to be checked to the rightmost position.
The code then performs a bitwise AND operation with 1 ((n >> i) & 1). 
This operation masks all bits except the rightmost bit, effectively checking if the rightmost bit is set to 1.
If the result of the bitwise AND operation is equal to 1, it means the bit being checked is set to 1, and c is incremented by 1.
After the loop completes, the code has counted the number of bits set to 1 in the binary representation of n, and the final count is returned.
TC=O(n)
SC=O(1)
'''
class Solution:
    def hammingWeight(self, n: int) -> int:
        c=0
        for i in range(32):
            if (((n>>i)&1)==1):
                c+=1
        return c
