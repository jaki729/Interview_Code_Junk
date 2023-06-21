'''
Initialize the variable length to store the length of nums.
If the length of nums is less than or equal to 2, reverse the list nums in-place and return. This handles the edge case where nums has 1 or 2 elements.
Set the pointer to the second last element (index length - 2).
Move the pointer towards the beginning of the list until we find a decreasing element or reach the beginning of the list. This is the point where the ascending order ends.
If the pointer reaches the beginning of the list (index -1), it means the entire list is in descending order. In this case, reverse the list in-place and return.
Find the smallest element in the suffix of nums that is greater than the element at the pointer. Swap these two elements.
Reverse the suffix of nums (starting from pointer + 1 index) in-place to make it in ascending order.
Time Complexity (TC):

The algorithm performs a linear scan from the second last element to find the pointer position, which takes O(N) time.
Reversing the suffix of nums takes O(N) time.
Overall, the time complexity is O(N), where N is the length of nums.
Space Complexity (SC):

The code uses a constant amount of extra space.
Therefore, the space complexity is O(1).
Note: The code assumes that nums is a list of integers and modifies it in-place.
'''
class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        length=len(nums)
        if length <= 2:
            return nums.reverse()
        # setting the pointer to the second last element
        pointer=length - 2
        # now moving the pointer until we find the ending of some sort in descending order
        while pointer >= 0 and nums[pointer] >= nums[pointer + 1]:
            pointer -=1 # decresing the value of pointer
        # if the pointer reaches zeroth index then value will have is -1
        if pointer == -1:
            return nums.reverse()
        # now we look to the number that comes after it
        # and iterate from the ending to the pointer
        for i in range(length-1 , pointer , -1):
            if nums[pointer] < nums[i]:
                # we are replacing the value less than the value of pointer
                nums[pointer], nums[i] = nums[i] , nums[pointer]
                break
        # now we take everything after pointer and make it ascending order 
        # this is done by reversing the order as it is faster
        nums[pointer + 1 : ] = reversed(nums[pointer + 1 : ])
