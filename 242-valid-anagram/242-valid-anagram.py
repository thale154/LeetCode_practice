class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashMap = {}
        for c in s:
            hashMap[c] = hashMap.get(c, 0) + 1
        for c in t:
            hashMap[c] = hashMap.get(c, 0) - 1
            if hashMap[c] < 0:
                return False
            
        return all(value == 0 for value in hashMap.values())
