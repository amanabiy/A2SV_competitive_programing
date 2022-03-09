class Solution:
    # def isValid(self, grid, row, col):
    #     return 0 <= row < len(grid) and 0 <= col < len(grid[row])
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.maxArea = 0
        self.directions = [(0,1), (0,-1), (1,0), (-1, 0)]
        n = len(grid)
        isValid = lambda row, col: 0 <= row < n and 0 <= col < len(grid[row]) and grid[row][col] == 1
        visited = set()
        
        def dfs(row, col):
            visited.add((row, col))
            area = 1
            for r, c in self.directions:
                newRow = row + r
                newCol = col + c
                if (newRow, newCol)  in visited or not isValid(newRow, newCol):
                    continue
                area += dfs(newRow, newCol)
            return area
        
        for row in range(n):
            for col in range(len(grid[row])):
                if (row, col) not in visited and isValid(row, col):
                    self.maxArea = max(self.maxArea, dfs(row, col))
                    
        return self.maxArea
