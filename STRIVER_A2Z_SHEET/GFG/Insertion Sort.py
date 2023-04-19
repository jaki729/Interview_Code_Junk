'''
https://practice.geeksforgeeks.org/problems/insertion-sort/0?category[]=Algorithms&page=1&query=category[]Algorithmspage1&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=insertion-sort

TC= O(N*N)
SC=O(1)
'''
#Sort the array using insertion sort

class Solution:
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, arr, n):
        #code here  
        # iterate from the second element to the end of the list
        for i in range(1, n):
            # assign the current element to a temporary variable
            temp=arr[i]
            j = i - 1
            # compare the current element with the elements to its left in the sorted list
            while j >= 0 and arr[j] >= temp:
                # if the current element is smaller than any of the elements to its left, swap it with that element
                arr[j+1] = arr[j]
                j -= 1 
            arr[j+1] = temp
        return arr
#{ 
 # Driver Code Starts
if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()
# } Driver Code Ends
