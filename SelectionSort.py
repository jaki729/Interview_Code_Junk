'''
Time Complexity		
Best					O(n2)
			
Worst					O(n2)
			
Average					O(n2)
			
Space Complexity		O(1)
			
Stability				No
logic
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
'''

def SelectionSort(nums):
    for i in range(len(nums)):
        min_index=i
        for j in range(i+1,len(nums)):
            if nums[min_index]>nums[j]:
                min_index=j
        nums[i],nums[min_index]=nums[min_index],nums[i]

print('Enter some numners. Type \'stop\' to stop input.')
nums=[]
while True:
    inp=input()
    if(inp=='stop'):
        break
    nums.append(int(inp))

print('Input list: ',nums)
SelectionSort(nums)
print('After slection sort: ', nums)