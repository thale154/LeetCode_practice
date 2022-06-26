class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        result, left, right = 0, 0, 0
        N = len(cardPoints) #Number of card
        # points of k cards at the right edge
        for i in range(k): right += cardPoints[N - i - 1]
        result = right
        for i in range(k):
            left += cardPoints[i]
            # N - k
            # N - k + 1
            # N - k + i
            right -= cardPoints[N - k + i]
            result = max(result, left + right)
        return result
        