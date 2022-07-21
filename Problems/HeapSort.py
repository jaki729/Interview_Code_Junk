'''
Time Complexity		
Best	O(nlog n)		
Worst	O(nlog n)		
Average	O(nlog n)	
Space Complexity	O(1)
Stability	No
Logic 
heapify(array)
    Root = array[0]
    Largest = largest( array[0] , array [2*0 + 1]. array[2*0+2])
    if(Root != Largest)
          Swap(Root, Largest)
void heapify(int arr[], int n, int i) {
  // Find largest among root, left child and right child
  int largest = i;
  int left = 2 * i + 1;
  int right = 2 * i + 2;

  if (left < n && arr[left] > arr[largest])
    largest = left;

  if (right < n && arr[right] > arr[largest])
    largest = right;

    // Swap and continue heapifying if root is not largest
    if (largest != i) {
      swap(&arr[i], &arr[largest]);
      heapify(arr, n, largest);
  }
}
// Build heap (rearrange array)
    for (int i = n / 2 - 1; i >= 0; i--)
      heapify(arr, n, i);
// Heap sort
    for (int i = n - 1; i >= 0; i--) {
      swap(&arr[0], &arr[i]);

      // Heapify root element to get highest element at root again
      heapify(arr, i, 0);
    }
'''
def MakeHeap(arr,n,i):
    largest=i
    l=2*i+1
    r=2*i+2

    if l<n and arr[i]<arr[l]:
        largest=l
    if r<n and arr[largest]<arr[r]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]

        MakeHeap(arr,n,largest)

def HeapSort(arr):
    n=len(arr)
    for i in range(n,-1,-1):
        MakeHeap(arr,n,i)
    for i in range(n-1,0,-1):
        arr[i],arr[0]=arr[0],arr[i]
        MakeHeap(arr,i,0)

print('Enter some numbers. Type \'stop\' to stop input.')
nums=[]
while True:
    inp=input()
    if(inp=='stop'):
        break
    nums.append(int(inp))

print('Input list:', nums)
HeapSort(nums)
print('After heap sort: ',nums)