def is_prime(number):
    if number<=1:
        return False
    for i in range (2,number):
        if number%i ==0:
            return False
    return True

print('Enter a number: ', end='')
num=int(input())

if is_prime(num):
    print(num, 'is a prime number')
else:
    print(num,'is not prime')