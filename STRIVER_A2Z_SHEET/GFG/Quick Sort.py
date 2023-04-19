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
'''
Hoare partition code
#!/usr/bin/env python
# coding=utf-8
import math

def merge(items, p, q, r):
    L = items[p:q+1]
    R = items[q+1:r+1]
    i = j = 0
    k = p
    while i < len(L) and j < len(R):
        if(L[i] < R[j]):
            items[k] = L[i]
            i += 1
        else:
            items[k] = R[j]
            j += 1
        k += 1
    if(j == len(R)):
        items[k:r+1] = L[i:]



def mergesort(items, p, r):
    if(p < r):
        q = math.floor((p+r)/2)
        mergesort(items, p, q)
        mergesort(items, q+1, r)
        merge(items, p, q, r)


items = [4,3,2,1,17]
mergesort(items, 0, len(items)-1)
print items
'''
