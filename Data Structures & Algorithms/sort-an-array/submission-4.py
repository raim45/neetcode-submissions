class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        k = 1
        while k < len(nums):
            i = 0
            while i < len(nums) - k:
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                i += 1
            k += 1
        return nums

#         Algorithm: BUBBLE_SORT(A, N)
# [A is an array of N elements]
# 1. Set K = 1
# 10.10 | Data Structures and Algorithms with C
# 2. Repeat steps 3 to 5 while K<N
# 3. Set I = 0
# 4. Repeat while I< = N - K then
# a) If A[I] > A[I+1] then
# Temp = A[I]
# A[I] = A[I+1]
# A[I+1] = Temp
# [End of If]
# b) Set I = I + 1
# [End of Loop]
# 5. Set K = K + 1
# [End of Loop]
# 6. Return
        