'''
https://practice.geeksforgeeks.org/problems/merge-sort/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=merge-sort

The time complexity of this implementation of merge sort is O(n log n), 
where n is the length of the input array. 
This is because the array is repeatedly divided into halves, and then merged back together in sorted order.
The space complexity of this implementation is O(n), 
where n is the length of the input array. 
This is because the merge function creates temporary arrays to hold the left and right halves of the array being merged. 
In the worst case, when the input array is already sorted in reverse order, 
these temporary arrays will be the same size as the original array. 
However, as soon as the merging is done and the function returns, the temporary arrays are deallocated, so the space usage is temporary.
'''
# import math module to use floor function
import math

# define a helper function to merge two sorted arrays
def merge(items, p, q, r):
    # slice the items array into two arrays L and R
    L = items[p:q+1]
    R = items[q+1:r+1]
    i = j = 0
    k = p
    # merge the two arrays while maintaining the sorted order
    while i < len(L) and j < len(R):
        if(L[i] < R[j]):
            items[k] = L[i]
            i += 1
        else:
            items[k] = R[j]
            j += 1
        k += 1
    # add the remaining elements of L or R to the merged array
    if(j == len(R)):
        items[k:r+1] = L[i:]

# define the main mergesort function
def mergesort(items, p, r):
    # base case: if the array has more than one element
    if(p < r):
        # find the middle index
        q = math.floor((p+r)/2)
        # recursively sort the left half
        mergesort(items, p, q)
        # recursively sort the right half
        mergesort(items, q+1, r)
        # merge the two sorted halves
        merge(items, p, q, r)

 '''
 according to clrs book
 #User function Template for python3
import math
class Solution:
    def merge(self,arr, l, m, r): 
        # code here
        n1 = m - l + 1
        n2 = r - m
         
        # create temporary arrays for left and right halves of the input array
        L = [0] * (n1)
        R = [0] * (n2)
        
        # copy data to the temporary arrays
        for i in range(0, n1):
            L[i] = arr[l + i]
            
        for j in range(0, n2):
            R[j] = arr[m + 1 + j]
    
        # Merge the temporary arrays back into arr[l..r]
        i = 0     # Initial index of first subarray
        j = 0     # Initial index of second subarray
        k = l     # Initial index of merged subarray
    
        while i < n1 and j < n2 :
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
    
        # Copy the remaining elements of L[], if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1
    
        # Copy the remaining elements of R[], if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1
            
        return arr       
    def mergeSort(self,arr, l, r):
        #code here
        if l < r:
            q = math.floor((l+r)/2)
            self.mergeSort(arr,l,q)
            self.mergeSort(arr,q+1,r)
            self.merge(arr,l,q,r)
'''
