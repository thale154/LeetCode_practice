class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashTable = {}
        for i, num in enumerate(numbers):
            if num in hashTable:
                return [hashTable[num], i + 1]
            hashTable[target - num] = i + 1
                