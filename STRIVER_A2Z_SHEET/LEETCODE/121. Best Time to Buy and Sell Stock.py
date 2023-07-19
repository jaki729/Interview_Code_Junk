'''
Initialize two pointers, lptr and rptr, to keep track of the buy and sell positions respectively. Initially, set lptr to 0 (the first index) and rptr to 1 (the next index).
Initialize the variable max_profit to store the maximum profit obtained.
Iterate through the list of prices using the rptr pointer until it reaches the end of the list.
Check if the price at the lptr index is less than the price at the rptr index. If it is, calculate the profit by subtracting the price at the lptr index from the price at the rptr index.
Update the max_profit variable with the maximum value between the current max_profit and the calculated profit.
If the price at the lptr index is greater than or equal to the price at the rptr index, it means the current price is lower than the previous buy price. In this case, update the lptr to the rptr index to consider the current price as the new buy price.
Increment the rptr pointer to move to the next index in the list.
After iterating through all the prices, return the max_profit.
Time Complexity (TC):

The algorithm performs a single pass through the list of prices.
Therefore, the time complexity is O(N), where N is the length of the prices list.
Space Complexity (SC):

The code uses a constant amount of extra space.
Therefore, the space complexity is O(1).
Note: The code assumes that prices is a list of integers representing the prices of stocks and returns the maximum profit that can be obtained.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # stock low buy and high sell gives profit
        #  lptr=buy and rptr=sell
        lptr , rptr = 0, 1
        max_profit=0
        while(rptr < len(prices)): # iterating through the list of prices
            if prices[lptr] < prices[rptr]:
                profit=prices[rptr] - prices[lptr]
                max_profit=max(max_profit , profit)
            else:
                lptr=rptr # when we find the lowest price 
                # we try to make left ptr to minimum
            rptr += 1
        return max_profit
