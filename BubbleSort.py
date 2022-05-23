'''
Time Complexity		
Best    	O(n)
			
Worst		O(n2)
			
Average		O(n2)
			
Space Complexity			O(1)
			
Stability	Yes
logic
bubbleSort(array)
  swapped <- false
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
      swapped <- true
end bubbleSort
'''
def BubbleSort(nums):
    n=len(nums)
    for i in range(n-1):
        for j in range(n-i-1):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]

print('Enter some numbers. Type \'stop\' to stop input.')
nums=[]
while True:
    inp=input()
    if(inp=='stop'):
        break
    nums.append(int(inp))

print('Input list: ', nums)
BubbleSort(nums)
print('After bubble sort: ', nums)