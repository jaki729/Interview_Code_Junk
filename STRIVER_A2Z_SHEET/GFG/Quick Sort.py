'''
https://practice.geeksforgeeks.org/problems/quick-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=quick-sort
The time complexity of Quick Sort is O(n*log(n)) on average 
and O(n^2) in worst case. 
The space complexity is O(log(n)) for recursive implementation
and O(n) for iterative implementation.
'''
#User function Template for python3

class Solution:
    def quickSort(self, arr, low, high):
        # Check if there are at least two elements to sort
        if low < high:
            # partition the array and sort left and right subarrays
            q = self.partition(arr, low, high)
            self.quickSort(arr, low, q - 1)
            self.quickSort(arr, q + 1, high)
    
    def partition(self, arr, low, high):
        # choose the last element as the pivot
        pivot = arr[high]
        i = low - 1
        # loop through the array and move elements smaller than pivot to the left
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        # swap the pivot with the element at i+1 index to place the pivot in its final position
        arr[i+1], arr[high] = arr[high], arr[i+1]
        return i+1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
