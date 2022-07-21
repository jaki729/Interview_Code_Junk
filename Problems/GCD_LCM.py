def gcd(a,b):
    if a==0:
        return b
    return gcd(b%a,a)

def lcm(a,b):
    return (a*b)/gcd(a,b)

print('Enter a number: ',end='')
n1=int(input())
print('Enter a number: ',end='')
n2=int(input())

print('LCM: ',lcm(n1,n2), 'GCD: ', gcd(n1,n2))
