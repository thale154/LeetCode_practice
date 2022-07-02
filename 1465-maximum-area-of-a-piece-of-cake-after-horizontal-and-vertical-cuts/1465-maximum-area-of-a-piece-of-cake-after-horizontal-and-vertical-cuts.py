class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.append(h)
        horizontalCuts.insert(0, 0)
        verticalCuts.sort()
        verticalCuts.append(w)
        verticalCuts.insert(0, 0)
        diffVertical = [verticalCuts[i] - verticalCuts[i-1] for i in range(1,len(verticalCuts))]
        diffHoriz = [horizontalCuts[i] - horizontalCuts[i-1] for i in range(1,len(horizontalCuts))]
        diffVertical.sort(reverse = True)
        diffHoriz.sort(reverse = True)
        return (diffVertical[0] * diffHoriz[0]) % (10**9 + 7)
        

        