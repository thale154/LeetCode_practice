class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')' : '(',
            ']' : '[',
            '}' : '{'
        }
        for c in s:
            if c in ['(','[','{']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if (top != match[c]):
                    return False
        if len(stack):
            return False
        return True
            