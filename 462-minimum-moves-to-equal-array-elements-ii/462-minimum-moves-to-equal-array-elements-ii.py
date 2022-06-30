class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        median = nums[len(nums) // 2]
        res = 0
        for num in nums: 
            res += abs(median - num)
        return res