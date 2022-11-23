'''
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
Example 1:
Input: rowIndex = 3
Output: [1,3,3,1]

Example 2:
Input: rowIndex = 0
Output: [1]

Example 3:
Input: rowIndex = 1
Output: [1,1]
The logic behind this problem is combinatorics maths that is nCr = (n!) / (r!*(n-r)!)
the formula that we going to apply is nCr / nCr-1 => (n-r+1) / r
=>nCr = (nCr-1) * ((n-r+1) / r) this formula is used to get the desired row_index values
'''
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # no matter what the first value of the triangle will be 1
        row=[1]
        for i in range(1, rowIndex + 1):
            row.append(row[i -1] * (rowIndex - i + 1) // i) # putting the formula into code 
        return row
