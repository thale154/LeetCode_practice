class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums = sorted(nums)
        median = nums[len(nums) // 2]
        
        return sum([abs(median - num) for num in nums]) 