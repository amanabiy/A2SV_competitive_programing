class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """
        Time: O(n) where n number of elements
        Space: O(k)
        """
        ans = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if len(ans) < k:
                    heapq.heappush(ans, -matrix[i][j])
                elif ans[0] < -matrix[i][j]:
                    heapq.heappop(ans)
                    heapq.heappush(ans, -matrix[i][j])
        return -ans[0]
