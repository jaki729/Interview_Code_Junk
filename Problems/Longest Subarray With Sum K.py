'''
https://www.codingninjas.com/studio/problems/longest-subarray-with-sum-k_5713505?utm_source=striver&utm_medium=website&utm_campaign=a_zcoursetuf&leftPanelTab=0
'''
# Method-1
def longestSubarrayWithSumK(nums: [int], k: int) -> int:
    # Create an empty dictionary to store the cumulative sum and its corresponding index.
    hashmap = {}
    # Initialize the maximum length to 0.
    max_len = 0
    # Initialize the cumulative sum variable to 0.
    s = 0
    
    # Iterate through the input list 'nums'.
    for i in range(len(nums)):
        # Calculate the cumulative sum by adding the current element to 's'.
        s += nums[i]
        
        # If the cumulative sum is equal to 'k', update 'max_len' with the current index + 1.
        if s == k:
            max_len = max(max_len, i + 1)
        
        # Calculate the remainder between the cumulative sum and 'k'.
        rem = s - k
        
        # If the remainder exists in the 'hashmap', it means there is a subarray with sum 'k' ending at index 'i'.
        # Calculate the length of this subarray and update 'max_len' if it is greater than the current value.
        if rem in hashmap:
            length = i - hashmap[rem]
            max_len = max(max_len, length)
        
        # If the current cumulative sum is not already in the 'hashmap', add it with its index 'i'.
        if s not in hashmap:
            hashmap[s] = i
    
    # Return the maximum length found.
    return max_len

# Time Complexity (TC): The code iterates through the input list 'nums' once, performing constant-time operations for each element.
# Therefore, the time complexity is O(n), where 'n' is the length of 'nums'.

# Space Complexity (SC): The code uses a dictionary 'hashmap' to store the cumulative sums and their corresponding indices.
# In the worst case, all cumulative sums up to index 'n' will be distinct, so the space complexity is O(n).

# Method 2:
def getLongestSubarray(nums: [int], k: int) -> int:
    l=0
    for i in range(len(nums)):
        s=0
        for j in range(i,len(nums)):
            s+=nums[j]
            if s==k:
                l=max(l,j-i+1)
    return l
