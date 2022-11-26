'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
No need to create another matrix just make the copy and do manipulation

Eample 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
TC=O(n) SC=(1)
'''
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # take two pointer left and right
        left , right = 0 , len(matrix)-1
        while left < right:
            for i in range(right-left): # iterating through the entire row except the last element
                # now take another two pointer
                top , bottom = left , right
                # storing the top left element
                top_left=matrix[top][left + i]
                # moving bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]
                # we are moving in clockwise direction but we are going in counter clockwise
                # moving bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]
                # moving top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]
                # moving top left to top right
                matrix[top + i][right] = top_left
            # update the pointer
            right -= 1
            left += 1
