class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)
        for ct in t_list:
            if not (s_list and t_list):
                break
            if ct == s_list[0]:
                s_list.pop(0)
        if not s_list:
            return True
        return False
            