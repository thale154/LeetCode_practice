class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        R, C = len(image), len(image[0])
        originalColor = image[sr][sc]
        def fillColor(row, col):
            if image[row][col] == color:
                return
            if image[row][col] == originalColor:
                image[row][col] = color
                if row >= 1: fillColor(row - 1, col) #top
                if row < R - 1: fillColor(row + 1, col) #bot
                if col >= 1: fillColor(row, col - 1) #left
                if col < C - 1: fillColor(row, col + 1) #right
        
        fillColor(sr, sc)
        return image
        
        