'''
https://practice.geeksforgeeks.org/problems/lcm-and-gcd4516/1

The time complexity of this code is O(log min(A,B)) 
which is the time complexity of the math.gcd() function used to calculate the GCD. 
The math.gcd() function uses the Euclidean algorithm to find the GCD of two numbers. 
The LCM is then calculated using the formula: LCM(A,B) = (A*B) / GCD(A,B).
Note that the math module has to be imported at the beginning of the code for this to work.
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def lcm(a, b):
    return (a * b) // gcd(a, b)

A = int(input())
B = int(input())

print(lcm(A, B), gcd(A, B))
'''
#User function Template for python3
import math
class Solution:
    def lcmAndGcd(self, A , B):
        # code here 
        lcm = (A * B) // math.gcd(A,B) 
        gcd = math.gcd(A , B)
        return [lcm , gcd]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        A,B=map(int,input().split())
        
        ob = Solution()
        ptr = ob.lcmAndGcd(A,B)
        
        print(ptr[0],ptr[1])
# } Driver Code Ends
