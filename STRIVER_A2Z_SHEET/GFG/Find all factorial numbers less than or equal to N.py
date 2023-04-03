'''
https://practice.geeksforgeeks.org/problems/find-all-factorial-numbers-less-than-or-equal-to-n3548/0?problemType=functional&difficulty[]=-1&page=1&query=problemTypefunctionaldifficulty[]-1page1&utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=find-all-factorial-numbers-less-than-or-equal-to-n
'''
class Solution:
    def factorialNumbers(self, N):
        #code here 
        fact = 1
        i = 2
        result = []
        while fact <= N:
            result.append(fact)
            fact*=i
            i+=1
        return result
