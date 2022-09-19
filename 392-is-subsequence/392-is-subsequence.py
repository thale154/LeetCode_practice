class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        for ct in t:
            if not (s_list):
                break
            if ct == s_list[0]:
                s_list.pop(0)
        if not s_list:
            return True
        return False
            