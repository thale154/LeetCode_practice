class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = prices[0]
        profit = 0
        for price in prices[1:]:
            minPrice = min(minPrice, price)
            profit = max(profit, price - minPrice)
        return profit