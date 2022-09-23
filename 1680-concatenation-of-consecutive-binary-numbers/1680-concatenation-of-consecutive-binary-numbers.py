class Solution:
    def concatenatedBinary(self, n: int) -> int:
        res = ''
        for i in range(1, n+1):
            res += format(i,"b")
        return int(res, 2) % (10**9 + 7)