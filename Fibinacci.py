def fib(n):
    if(n<=1):
        return n
    return fib(n-2) + fib(n-1)

print('Enter a number: ', end=' ')
num=int(input())
print('Nth fibonacci number is: ',fib(num))