from collections import Counter
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        result=[]
        feq=Counter(arr1)
        for element in arr2:
            result.extend([element]*feq[element])
            feq[element]=0
        remaining_elements=list(sorted(filter(lambda x: feq[x]!=0,feq.keys())))
        for element in remaining_elements:
            result.extend([element]*feq[element])
        return result
