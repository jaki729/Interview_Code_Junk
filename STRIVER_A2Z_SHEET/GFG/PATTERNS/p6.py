'''
Input: 5

Output:
1 2 3 4 5
1 2 3 4
1 2 3 
1 2  
1
'''
#User function Template for python3

class Solution:
    def printTriangle(self, N):
        # Code here
        for i in range(N,0,-1):
            for j in range(1,i+1):
                print(j,end=" ")
            print()


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ob.printTriangle(N)
# } Driver Code Ends
