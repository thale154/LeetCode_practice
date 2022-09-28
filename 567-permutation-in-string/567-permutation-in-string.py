class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def permutationSubstring(s1Hash: dict, subs2: str) -> bool:
            copys1Hash = s1Hash.copy()
            for c in subs2:
                if c not in copys1Hash:
                    return False
                copys1Hash[c] -= 1
                if copys1Hash[c] < 0:
                    return False
            return True
        
        s1Hash = {}
        lens1 = len(s1)
        for c in s1:
            s1Hash[c] = s1Hash.get(c, 0) + 1
        for i in range(len(s2) - lens1 + 1):
            if permutationSubstring(s1Hash, s2[i: i+lens1]):
                return True
        return False
            
        