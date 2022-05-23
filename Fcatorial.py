def factorial(number,total=1):
    if(number<2):
        return total
    return factorial(number-1,total*number)

print('Enter a number: ',end=' ');
num=int(input())
result=factorial(num)
print('Factorial of ',num,' is ', result)