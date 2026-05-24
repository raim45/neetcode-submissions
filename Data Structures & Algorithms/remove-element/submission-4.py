class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums == []:
            return 0
        
        hashmap = {}
        for i, value in enumerate(nums):
            hashmap[value] = 1 + hashmap.get(value, 0)
        if val in hashmap:
            del hashmap[val]
         
        res = []
        for i, val in hashmap.items():
                res += [i] * val
        for i in range(len(res)):
            nums[i] = res[i]
        return len(res)
        



        