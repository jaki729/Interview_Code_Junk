'''
https://leetcode.com/problems/single-number/description/
'''
# Method-1
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0  # Initialize the variable 'xor' to 0

        for i in range(len(nums)):  # Loop through each element in 'nums'
            xor ^= nums[i]  # Bitwise XOR operation between 'xor' and the current element in 'nums'

        return xor  # Return the result of XOR operation

# Time Complexity (TC): The loop runs 'n' times (where 'n' is the length of the input 'nums').
# Each iteration of the loop takes constant time to perform the XOR operation.
# Therefore, the overall Time Complexity is O(n).

# Space Complexity (SC): The code uses only a single variable 'xor' to store the result of XOR operation.
# No additional space is used based on the input size 'n'.
# Hence, the Space Complexity is O(1), which is constant space.

# Method 2
# tc =sc O(n)
def getSingleElement(arr: List[int]) -> int:
    # Create an empty hashmap to store the count of occurrences of each element
    hashmap = {}
    
    # Traverse the array and count the occurrences of each element
    for num in arr:
        # Check if the element is already present in the hashmap
        # If present, increment the count by 1; otherwise, set count to 1
        hashmap[num] = hashmap.get(num, 0) + 1
    
    # Traverse the hashmap to find the element that occurs only once
    for num, count in hashmap.items():
        if count == 1:
            # Return the element that occurs only once
            return num
    
    # If no element occurs only once, return -1
    return -1
