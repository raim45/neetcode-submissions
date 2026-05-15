class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # sorted approach
        # hashmap = {}

        # for i in nums:
        #     hashmap[i] = 1 + hashmap.get(i, 0)
            
        # arr = []
        # for i, val in hashmap.items():
        #     arr.append([val, i])
        # res =[]
        # while len(res) < k:
        #     res.append(arr.pop()[1])

        # return res


        hashmap = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            hashmap[i] = 1 + hashmap.get(i, 0)
        for i, val in hashmap.items():
            freq[val].append(i)
        res = []

        for i in range(len(freq) - 1, 0, -1):
            for each in freq[i]:
                res.append(each)
                if len(res) ==k:
                    return res


