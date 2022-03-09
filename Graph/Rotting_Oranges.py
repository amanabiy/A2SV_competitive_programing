class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        self.timeToRotten = 0
        n = len(grid)
        visited = set()
        directions = [(1,0), (-1,0), (0, 1), (0,-1)]
        isValid = lambda r, c: 0 <= r < n and 0 <= c < len(grid[r]) and (grid[r][c] == 1 or grid[r][c] == 2) and (r, c) not in visited
        queue = deque()
        
        
        for i in range(n):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j))
                    visited.add((i,j))

        while queue:
            found = False
            ns = len(queue)
            for _ in range(ns):
                row, col = queue.popleft()
                for r, c in directions:
                    newRow, newCol = row + r, col + c
                    if isValid(newRow, newCol):
                        queue.append((newRow, newCol))
                        visited.add((newRow, newCol))
                        if grid[newRow][newCol] == 1:
                            found = True
                            grid[newRow][newCol] = 2
            if found:
                self.timeToRotten += 1

        for i in range(n):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1

        return self.timeToRotten
                    
                    
        
