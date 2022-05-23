'''
Time Complexity	
Best	O(n)		
Worst	O(n2)		
Average	O(n2)
			
Space Complexity		O(1)
			
Stability	Yes
logic
insertionSort(array)
  mark first element as sorted
  for each unsorted element X
    'extract' the element X
    for j <- lastSortedIndex down to 0
      if current element j > X
        move sorted element to the right by 1
    break loop and insert X here
end insertionSort
'''
def InsertionSort(nums):
    for i in range(1,len(nums)):
        key=nums[i]
        j=i-1
        while j>=0 and key<nums[j]:
            nums[j+1]=nums[j]
            j=j-1
        nums[j+1]=key

print('Enter some numbers. Type \'stop\' to stop input.')
nums=[]
while True:
    inp=input()
    if(inp=='stop'):
        break
    nums.append(int(inp))

print('Input list: ',nums)
InsertionSort(nums)
print('After insertion sort:' , nums)