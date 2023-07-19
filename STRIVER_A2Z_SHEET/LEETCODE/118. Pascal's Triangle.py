'''
https://leetcode.com/problems/pascals-triangle/
Initialize ans with the base case:

ans is a 2D list initialized with a single row containing the value 1. This represents the first row of Pascal's Triangle.
Building rows:

Iterate from 0 to numRows - 1, as we already have the first row.
For each iteration, create a temporary list temp that represents the row above the current row in Pascal's Triangle. It is obtained by adding two pointers with a value of 0 at the beginning and end of the previous row.
Create an empty list row to store the values of the current row being constructed.
Calculate values for the current row:

Iterate from 0 to the length of the previous row (len(ans[-1])) plus 1. This allows us to iterate over the elements of temp and calculate the values for the current row.
For each element at index j, calculate the value by adding the current element (temp[j]) and the next element (temp[j + 1]) in temp. This sum represents the value obtained from the row above.
Append the calculated value to the row list.
Append the current row to ans:

After calculating all the values for the current row, append the row list to ans.
Repeat steps 2-4 for the specified number of rows (numRows).

Return the generated Pascal's Triangle (ans).

Time Complexity (TC):

The code iterates through each row from 0 to numRows - 1. For each row, the number of operations depends on the length of the previous row (len(ans[-1])).
Therefore, the time complexity is approximately O(numRows^2).
Space Complexity (SC):

The code uses space to store the Pascal's Triangle in the ans list, which has numRows rows.
Therefore, the space complexity is approximately O(numRows^2).
Note: The code assumes that numRows is a non-negative integer.
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
