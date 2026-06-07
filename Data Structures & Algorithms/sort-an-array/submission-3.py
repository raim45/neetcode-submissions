class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(len(nums)):
            val = min(nums)
            res.append(val)
            nums.remove(val)
        return res
    
        