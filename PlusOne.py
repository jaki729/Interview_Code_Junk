class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else: 
                #for 10
                digits[i] = 0
        digits.insert(0, 1)
        return digits
