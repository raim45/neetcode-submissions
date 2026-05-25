class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums) / 2

        for i, val in enumerate(nums):
            hashmap[val] = 1 + hashmap.get(val, 0)

        for i, val in hashmap.items():
            if val > n:
                return i
        