class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        median = nums[n // 2]
        res = 0
        for num in nums: 
            res += abs(median - num)
        return res