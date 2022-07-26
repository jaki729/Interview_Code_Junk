#m1
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))
#m2
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
