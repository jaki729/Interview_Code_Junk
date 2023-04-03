'''
https://practice.geeksforgeeks.org/problems/armstrong-numbers2727/1

Time Complexity: O(n) where n is the number of digits since we need to traverse every digit and add digits raised to power no. of digits to sum.

Space Complexity: O(1) since no extra space is required
'''
#User function Template for python3
class Solution:
    def armstrongNumber (ob, n):
        # code here 
        original_number = n
        count = 0
        temp = n
        while temp != 0:
            count += 1
            temp //= 10
        sum_digit_pow = 0
        while n != 0:
            digit = n % 10
            sum_digit_pow += pow(digit , count)
            n //= 10
        if sum_digit_pow == original_number:
            return "Yes"
        return "No"

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends
