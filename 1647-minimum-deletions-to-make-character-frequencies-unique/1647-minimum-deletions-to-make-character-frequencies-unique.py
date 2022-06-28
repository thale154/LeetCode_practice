class Solution:
    def minDeletions(self, s: str) -> int:
        # frequency and each distinct character
        mp = {}
        # frequency
        pq = []
        
        count = 0
        
        # each character in s
        for c in s:
            mp[c] = mp.get(c, 0) + 1
        
        for i in mp:
            pq.append(mp[i])
        
        # the largest frequency at the top
        pq = sorted(pq)
        
        while pq:
            frequency = pq[-1]
            del pq[-1]
            
            if (len(pq) == 0):
                return count
            
            if frequency == pq[-1]:
                if frequency > 1:
                    pq.append(frequency - 1)
                
                count += 1
                
            pq = sorted(pq)
            
        return cnt