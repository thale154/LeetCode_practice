class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        if n == 1:
            return 1
        candies = [1] * n
        
         #left to right
        for i in range(n-1):
            if ratings[i] < ratings[i+1]:
                candies[i+1] = candies[i] + 1
                
        #right to left
        for i in range(n-1, 0, -1): 
            if ratings[i] < ratings[i-1]:
                candies[i - 1] = max(candies[i-1], candies[i] + 1)
                
        return sum(candies)