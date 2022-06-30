class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        median = sorted(nums)[n // 2]
        res = sum([abs(median - num) for num in nums])
        return res