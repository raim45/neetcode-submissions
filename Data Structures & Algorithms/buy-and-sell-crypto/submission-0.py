class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if( not prices):
            return 0
        price = []
        maxi = 0  
        for i in prices:
            if(len(price) == 0):
                price.append(i)
                continue
            val = i - min(price)
            if val >maxi:
                maxi = val
            price.append(i)
        return maxi



        