https://practice.geeksforgeeks.org/problems/count-digits5716/1
'''
Given a number N. Count the number of digits in N which evenly divides N.
Note :- Evenly divides means whether N is divisible by a digit i.e. leaves a remainder 0 when divided.
Example 1:
Input:
N = 12
Output:
2
Explanation:
1, 2 both divide 12 evenly
Example 2:
Input:
N = 23
Output
0
Explanation:
2 and 3, none of them
divide 23 evenly
'''
#User function Template for python3
import math

class Solution:
    def evenlyDivides (self, n):
        # code here
        count = 0
        for digit in str(n):
            if digit != '0' and n % int(digit) == 0:
                count += 1
        return count

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
'''
The time complexity of the above algorithm is O(d log N), 
where d is the number of digits in N. Since we need to iterate over each digit in N and perform a modulus operation on each digit, 
the time complexity is proportional to the number of digits in N.
The log N factor is due to the fact that we need to calculate the logarithm of N in base 10 to determine the number of digits.
'''
