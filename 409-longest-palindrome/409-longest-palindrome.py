class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashTable = {}
        for c in s:
            hashTable[c] =  hashTable.get(c, 0) + 1
        res = sum([value//2 for value in hashTable.values()]) #số chẵn các kí tự: ví dụ 4 -> 2, 5 -> 2
        if 1 in [value%2 for value in hashTable.values()]:
            res = res * 2 + 1
        else:
            res *= 2
        return res