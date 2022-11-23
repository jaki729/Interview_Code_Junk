'''
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
Example 1:
Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:
Input: numRows = 1
Output: [[1]]
The time complexity and space complexity is O(n^2).
working logic    010
                 0110
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]] # base case, the first value of triangle

        for i in range(numRows - 1): #building of rows
            temp=[0] + ans[-1] + [0] # adding two ptrs at the begining and end having value=0 
            # then building the next empty row to iterate over and get the value of next row
            row=[]
            for j in range(len(ans[-1])+1): 
                row.append(temp[j] + temp[j + 1]) # adding and getting the value from above 
                # and appending it to ans[]
            ans.append(row)
        return ans
