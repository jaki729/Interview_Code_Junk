class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(filter(str.isalnum,s))
        return s.lower()==s[::-1].lower()
