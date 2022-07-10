class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if cost[1] <= cost[0]:
            d = deque([(cost[1], 1)])
        else:
            d = deque([(cost[0], 0), (cost[1], 1)])

        for i in range(2, len(cost)):
            temp = cost[i] + d[0][0]
            while d and temp <= d[-1][0]:
                d.pop()
            d.append([temp, i])
            if i - d[0][1] == 2:
                d.popleft()

        return d[0][0]