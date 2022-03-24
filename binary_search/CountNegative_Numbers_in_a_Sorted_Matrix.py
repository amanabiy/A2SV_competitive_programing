class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        countNegative = 0
        for i in range(len(grid)):
            left = 0
            right = len(grid[i]) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if grid[i][mid] < 0:
                    right = mid - 1
                else:
                    left = mid + 1
            countNegative += len(grid[i]) - left
                    
        return countNegative
