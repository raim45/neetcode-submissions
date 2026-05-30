class Solution:
    def maxArea(self, heights: List[int]) -> int:
        if heights == []:
            return 0
        con = float("-inf")
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                width = j-i
                length = min(heights[i], heights[j])
                vol = width * length
                if vol > con:
                    con = vol
        return con


    





        