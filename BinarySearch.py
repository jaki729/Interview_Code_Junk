'''
Time Complexities
    Best case complexity: O(1)
    Average case complexity: O(log n)
    Worst case complexity: O(log n)
Space Complexity
The space complexity of the binary search is O(1)

Logic
do until the pointers low and high meet each other.
    mid = (low + high)/2
    if (x == arr[mid])
        return mid
    else if (x > arr[mid]) // x is on the right side
        low = mid + 1
    else                       // x is on the left side
        high = mid - 1
'''
def BinarySearch(nums,x,low,high):
    while low <= high:

        mid = low + (high - low)//2

        if nums[mid] == x:
            return mid

        elif nums[mid] < x:
            low = mid + 1

        else:
            high = mid - 1

    return -1

print(' Enter some numbers. Type \'stop\' to stop input.')
nums=[]
while True:
    inp=input()
    if(inp=='stop'):
        break
    nums.append(int(inp))
print('Enter a number to search: ', end=' ')
x=int(input())
print('Input list: ',nums,',searching for : ',x)
result=BinarySearch(nums,x,0,len(nums))
if(result==-1):
    print('The number was not found')
else:
    print('Found it at location: ', result)
