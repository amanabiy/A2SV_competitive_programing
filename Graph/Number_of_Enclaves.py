class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        directions = [(0,1),(1,0),(-1,0),(0,-1)]
        isValid = lambda r, c: 0 <= r < n and 0 <= c < m 
        isOnBoarder = lambda r, c: r < 0 or r >= n or c < 0 or c >= m
    
    
        def dfs(row, col):
            grid[row][col] = 0
            for r, c in directions:
                newRow, newCol = row + r, col + c
                if isValid(newRow, newCol) and grid[newRow][newCol] == 1:
                    dfs(newRow, newCol)
    
    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    continue
                for r, c in directions:
                    newRow, newCol = i + r, j + c
                    if isOnBoarder(newRow, newCol):
                        dfs(i, j)
                        break
    
    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    count += 1
                    

        return count
