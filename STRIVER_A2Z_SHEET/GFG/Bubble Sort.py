'''
https://practice.geeksforgeeks.org/problems/bubble-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=bubble-sort
'''
#User function Template for python3

class Solution:
    #Function to sort the array using bubble sort algorithm.
    def bubbleSort(self,arr, n):
        # code here
        # Traverse through all array elements
        for i in range(n):
            # Flag to detect if any swapping occurs
            swap =  False
            # Last i elements are already in place
            for j in range(0 , n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
                if arr[j] > arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
                    swap = True
            # If no two elements were swapped by inner loop, break
            if not swap:
                break
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.bubbleSort(arr, n)
        for i in arr:
            print(i,end=' ')
        print()

# } Driver Code Ends
