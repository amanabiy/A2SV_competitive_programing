class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:

        def dfs(row, col):
            if start_value == newColor:
                return
            image[row][col] = newColor
            for r, c in neighbors:
                currRow, currCol = row + r, col + c
                if not isInLimit(currRow, currCol) or image[currRow][currCol] != start_value:
                    continue
                dfs(currRow, currCol)

        n = len(image)
        m = len(image[0]) if image else 0
        start_value = image[sr][sc]
        neighbors = [(0,-1), (0,1), (1,0), (-1,0)]
        isInLimit = lambda x, y: 0 <= x < n and 0 <= y < m

        dfs(sr, sc)

        return image
