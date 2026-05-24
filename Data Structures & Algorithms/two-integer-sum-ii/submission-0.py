class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, val in enumerate(numbers):
            nval = target - val
            if nval in hashmap:
                return [hashmap[nval], i + 1]
            hashmap[val] = i + 1
        