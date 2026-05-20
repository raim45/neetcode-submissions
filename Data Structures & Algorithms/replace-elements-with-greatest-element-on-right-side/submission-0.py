class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # n = len(arr)
        # maxright = []
        # for i in range(len(arr) - 1):
        #     maxs = float("-inf")
        #     for j in range(i+1, len(arr)):
        #         if j > maxs:
        #             maxs = j
        #     maxright.append(j)
        
        # maxright[n - 1] = -1
        # return maxright
        [2,4,5,3,1,2]
        
        for i in range(len(arr) - 1):
            temp = arr[i+1:]
            arr[i] = max(temp)
        arr[-1] = -1
        return arr


