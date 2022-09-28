class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        hashTable = {}
        res = 0
        indexFirstC = 0 # index of first character in substring
        # key: character
        # value: index of last found character
        for i,c in enumerate(s):
            if c in hashTable:
                indexFirstC = max(hashTable[c] + 1, indexFirstC)
            hashTable[c] = i
            res = max(res, i - indexFirstC + 1)
        return res
