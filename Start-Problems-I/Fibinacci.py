#m1
def fib(n):
    if(n<=1):
        return n
    return fib(n-2) + fib(n-1)

print('Enter a number: ', end=' ')
num=int(input())
print('Nth fibonacci number is: ',fib(num))

#m2
class Solution:
    def fib(self, n: int) -> int:
        a=0
        b=1
        if n==0:
            return a
        elif n==1:
            return b
        else:
            for i in range(1, n):
                c = a + b
                a = b
                b = c
            return b
 
#m3
class Solution:
    def fib(self, n: int) -> int:
        if n==0 or n==1:
            return n
        else:
            return (self.fib(n-1)+self.fib(n-2))
