class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, num in enumerate(nums):
            if num in hashTable:
                return [i, hashTable[num]]
            hashTable[target - num] = i