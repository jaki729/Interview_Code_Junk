from math import *
def prime_check(n):
    if n == 1:
        return False
    for i in range(2,ceil(sqrt(n))+1):
        if n%i==0:
            return False
        return True

n=int(input())
ans=prime_check(n)
if ans:
    print("The number is Prime")
else:
    print("The number is not Prime")