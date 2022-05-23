'''
Time Complexity		
Best	O(n*log n)		
Worst	O(n2)		
Average	O(n*log n)	
Space Complexity	O(log n)
Stability	No
Logic
quickSort(array, leftmostIndex, rightmostIndex)
  if (leftmostIndex < rightmostIndex)
    pivotIndex <- partition(array,leftmostIndex, rightmostIndex)
    quickSort(array, leftmostIndex, pivotIndex - 1)
    quickSort(array, pivotIndex, rightmostIndex)

partition(array, leftmostIndex, rightmostIndex)
  set rightmostIndex as pivotIndex
  storeIndex <- leftmostIndex - 1
  for i <- leftmostIndex + 1 to rightmostIndex
  if element[i] < pivotElement
    swap element[i] and element[storeIndex]
    storeIndex++
  swap pivotElement and element[storeIndex+1]
return storeIndex + 1
'''
def partition(arr,low,high):
    i=(low-1)
    pivot=arr[high]

    for j in range(low,high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1

def QuickSort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)

        QuickSort(arr,low,pi-1)
        QuickSort(arr,pi+1,high)

print('Enter some numners. Type \'stop\' to stop input.')
nums=[]
while True:
    inp=input()
    if(inp=='stop'):
        break
    nums.append(int(inp))

print('Input list: ', nums)
QuickSort(nums,0,len(nums)-1)
print('After quick sort: ', nums)
