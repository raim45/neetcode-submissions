class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
       
        [2,4,5,3,1,2]
        
        for i in range(len(arr) - 1):
            temp = arr[i+1:]
            arr[i] = max(temp)
        arr[-1] = -1
        return arr


