class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[0] * x for x in range(1, numRows+1)]
        for row in range(numRows):
            for col in range(row + 1):
                if (col == 0) or (col == row):
                    res[row][col] = 1
                else:
                    res[row][col] = res[row-1][col-1] + res[row-1][col]
        return res