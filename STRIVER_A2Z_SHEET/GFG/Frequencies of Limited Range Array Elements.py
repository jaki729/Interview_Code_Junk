'''
https://practice.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0
TC = O(n)
'''
class Solution:
    # Define a function called frequencyCount that takes in three parameters:
    # an array called arr, an integer called n, and an integer called p
    def frequencyCount(self, arr, n, p):
        
        # Create an empty hashmap called freq_map
        freq_map = {}
        
        # Traverse the array and increment the count of each element in the hashmap
        for i in range(N):
            if arr[i] in freq_map: # if the element already exists in the hashmap
                freq_map[arr[i]] += 1 # increment its count by 1
            else: # if the element does not exist in the hashmap
                freq_map[arr[i]] = 1 # add it to the hashmap with a count of 1
        
        # Traverse the array again
        for i in range(n):
            if i+1 in freq_map: # if the value i+1 is in the hashmap
                arr[i] = freq_map[i+1] # set the corresponding element in the array to the count of that value in the hashmap
            else: # if the value i+1 is not in the hashmap
                arr[i] = 0 # set the corresponding element in the array to 0
