class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        S = sum(nums)
        leftSum = 0
        for i, num in enumerate(nums):
            if leftSum == (S - leftSum - num): # = rightSum
                return i
            leftSum += num
        return -1