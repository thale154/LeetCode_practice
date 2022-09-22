class Solution:
    def reverseWords(self, s: str) -> str:
        word = ''
        res = ''
        for c in s:
            if c == ' ':
                res += word + ' '
                word = ''
            else:
                word = c + word
        res += word
        return res
            