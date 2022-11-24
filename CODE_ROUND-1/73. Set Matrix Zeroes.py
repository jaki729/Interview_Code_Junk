'''
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row,col=len(matrix),len(matrix[0])
        row_zero=False

        # determining which row or column needs to be zero
        for r in range(row):
            for c in range(col):
                if matrix[r][c] == 0:
                    matrix[0][c]=0
                    if r>0:
                        matrix[r][0]=0
                    else:
                        row_zero=True
        
        # we make zero most of the row or columns that are possible
        for r in range(1,row):
            for c in range(1,col):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c]=0

        # we are zeroing out the first column to 0 if required
        if matrix[0][0] == 0:
            for r in range(row):
                matrix[r][0]=0

        # we are zeroing out the first row to 0 if required
        if row_zero:
            for c in range(col):
                matrix[0][c]=0
