'''
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, 
then the next permutation of that array is the permutation that follows it in the sorted container.
If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).
For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

Example 1:
Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:
Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:
Input: nums = [1,1,5]
Output: [1,5,1]
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
