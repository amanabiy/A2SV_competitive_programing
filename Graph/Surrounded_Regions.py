class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = set()
        directions = [(0,1), (1,0),(0,-1),(-1,0)]
        n = len(board)
        isFlipped = lambda r, c: 0 <= r < n and 0 <= c < len(board[0]) 
        
        def dfs(row, col):
            visited.add((row, col))
            for r, c in directions:
                newRow, newCol = row + r, col + c
                if isFlipped(newRow, newCol) and board[newRow][newCol] == 'O' and (newRow, newCol) not in visited:
                    dfs(newRow, newCol)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                isOnBoarder = False
                if board[i][j] == 'O':
                    for r, c in directions:
                        newRow, newCol = i + r, j + c
                        if  not isFlipped(newRow, newCol):
                            isOnBoarder = True
                if isOnBoarder:
                    dfs(i, j)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 'O'  and (i, j) not in visited:
                    board[i][j] = 'X'
