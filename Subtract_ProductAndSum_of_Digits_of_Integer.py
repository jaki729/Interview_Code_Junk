class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        s=0
        prod=1
        while n:
            n, digit = divmod(n, 10)
            s+=digit
            prod*=digit
        result = prod-s
        return result
