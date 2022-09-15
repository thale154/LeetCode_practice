class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = sumRes = nums[0]
        for num in nums[1:]:
            sumRes = max(num, sumRes + num)
            maxSum = max(maxSum, sumRes)
        return maxSum
