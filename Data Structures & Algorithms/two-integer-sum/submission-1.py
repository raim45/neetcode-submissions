class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # original brute force
        # for i in range(len(nums)):
        #     value = target - nums[i]
        #     for k in range(i +1, len(nums)):
        #         if(nums[k] == value):
        #             return [i, k]

        # using hash maps
        hast = {}
        
        for i, val in enumerate(nums):
            if(target - val in hast):
                return [hast[target - val], i]
            hast[val] = i


        