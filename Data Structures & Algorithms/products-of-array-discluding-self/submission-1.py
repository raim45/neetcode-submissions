class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rest = []
        product = 1
        zero_count = 0
        if nums == []:
            return []
        for i in nums:
            if i == 0:
                zero_count += 1
                continue
            product *= i

        for i in nums:
            if i == 0:
                if zero_count > 1:
                    rest.append(0)
                else:
                    rest.append(round(product))
            elif zero_count >= 1:
                rest.append(0)
            else:
                rest.append(round(product / i))
        return rest 
        