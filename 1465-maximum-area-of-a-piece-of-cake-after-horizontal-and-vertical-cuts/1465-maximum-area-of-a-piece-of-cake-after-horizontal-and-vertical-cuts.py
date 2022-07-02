class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts.append(h)
        verticalCuts.sort()
        verticalCuts.append(w)
        
        max_height = 0
        max_width = 0
        top = 0
        for bottom in horizontalCuts:
            max_height = max(max_height, bottom - top)
            top = bottom
        left = 0
        for right in verticalCuts:
            max_width = max(max_width, right - left)
            left = right

        return (max_height * max_width) % (10**9 + 7)
        

        