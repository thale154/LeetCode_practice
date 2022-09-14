class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re
        cleaned = re.sub(r'[^a-z0-9]', '', s.lower())
        for i in range(len(cleaned)//2):
            if (cleaned[i] != cleaned[len(cleaned)-i-1]):
                return False
        return True