class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        maxval = 0
        for i in hashset:
            
            if (i -1) not in hashset:
                i
            else:
                continue
            count = 1
            val = i
            while val + 1 in hashset:
                count += 1
                val += 1

            if count > maxval:
                maxval = count
        return maxval





        
