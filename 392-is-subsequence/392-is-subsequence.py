class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        len_s = len(s)
        i = 0
        for ct in t:
            if i == len_s:
                break
            if ct == s[i]:
                i += 1
        if i == len_s :
            return True
        return False
            