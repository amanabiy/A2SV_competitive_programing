class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        self.visited = set()
        self.totalProvince = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        checkValidity = lambda x, y: 0 <= x < n and 0 <= y < n
        
        def dfs(row):
            self.visited.add(row)
            for j in range(len(isConnected[row])):
                if j not in self.visited and j!=row and isConnected[row][j] == 1:
                    dfs(j)

        n = len(isConnected)
        for i in range(n):
            if i not in self.visited:
                dfs(i)
                self.totalProvince += 1

        return self.totalProvince        
