'''
https://leetcode.com/problems/valid-palindrome/
The time complexity of the given code is O(n), 
where n is the length of the string. 
This is because each character in the string is visited once in the recursive calls.
The space complexity of the code is O(n) as well, 
as each recursive call adds a new activation record on the stack, 
which contains information about the current position in the string. 
Therefore, the space used on the stack is proportional to the length of the string.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower() # make the whole phrase into lower-case
        s = ''.join(ch for ch in s if ch.isalnum()) # remove all non alpha numeric characters
        return s == s[::-1] # check euality
