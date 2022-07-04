class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        candies = [1] * n
        for i in range(n-1): #left to right
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1
        for i in range(n-1, 0, -1): #right to left
            if ratings[i] < ratings[i-1]:
                candies[i - 1] = max(candies[i-1], candies[i] + 1)
        return sum(candies)