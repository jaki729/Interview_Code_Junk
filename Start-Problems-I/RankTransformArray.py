class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        newArray=arr.copy()
        newArray.sort()
        ranks={}
        rank=1
        for index in range(len(newArray)):
            element=newArray[index]
            if element not in ranks:
                ranks[element]=rank
                rank+=1
        for index in range(len(arr)):
            element=arr[index]
            arr[index]=ranks[arr[index]]
        return arr
