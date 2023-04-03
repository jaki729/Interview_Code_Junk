'''
https://practice.geeksforgeeks.org/problems/sum-of-all-divisors-from-1-to-n4738/1
The time complexity of the given code is O(N) as the for loop runs from 1 to N to compute the sum of divisors. 
However, since the loop is executed only once, 
the overall time complexity of the given code is O(1) in terms of N.
'''
#User function Template for python3


class Solution:
    def sumOfDivisors(self, n):
    	#code here 
        sum = 0 
        for i in range(1,n+1):
            sum += (n//i)*i
        return int(sum)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends
