class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        median = nums[n // 2]
        
        return sum([abs(median - num) for num in nums]) 