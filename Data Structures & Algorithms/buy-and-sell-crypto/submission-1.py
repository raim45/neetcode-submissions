class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if( not prices):
            return 0
        maxi = 0  
        mini = float("inf")
        for i in prices:
            if(i < mini):
                mini = i
            val = i - mini
            if val >maxi:
                maxi = val
        return maxi



        