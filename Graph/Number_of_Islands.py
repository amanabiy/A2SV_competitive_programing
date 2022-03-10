class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numberIsland = 0
        directions = [(0,1),(1,0), (-1,0), (0,-1)]
        n, m = len(grid), len(grid[0])
        isValid = lambda r, c: 0 <= r < n and 0 <= c < m
        
        def dfs(row, col):
            grid[row][col] = "0"
            for r, c in directions:
                newRow, newCol = row + r, col + c
                if isValid(newRow, newCol) and grid[newRow][newCol] == '1':
                    dfs(newRow, newCol)
                    
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i, j)
                    numberIsland += 1

        return numberIsland
                    
