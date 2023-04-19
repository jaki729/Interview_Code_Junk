'''
https://practice.geeksforgeeks.org/problems/selection-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=selection-sort
Time Complexity: O(N^2)
Auxiliary Space: O(1)
'''

class Solution: 
    def selectionSort(self, arr, n):
        # iterate through the array
        for i in range(n):
            # initialize the minimum index as the current index
            min_index = i
            # iterate through the unsorted portion of the array to find the minimum element
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j
            # swap the minimum element with the first element of the unsorted portion of the array
            arr[i], arr[min_index] = arr[min_index], arr[i]
        # return the sorted array
        return arr
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
