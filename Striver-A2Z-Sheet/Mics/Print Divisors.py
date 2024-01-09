'''
Time Complexity: O(sqrt(n)), because every time the loop runs only sqrt(n) times.

Space Complexity: O(1), we are not using any extra space.
'''
def printDivisors(n):
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            print(i)
            if i!=n/i:
                print(int(n/i))
    print()
if __name__=="__main__":
    printDivisors(36)