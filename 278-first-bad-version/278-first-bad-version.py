# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        right = n
        left = 1
        while (left <= right):
            mid = (left + right)//2
            if (isBadVersion(mid) == True): #is bad
                right = mid - 1
            else:
                left = mid + 1
        return left
            
            