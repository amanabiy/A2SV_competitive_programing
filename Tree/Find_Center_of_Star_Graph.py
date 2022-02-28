class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        """
        """
        ans = [*edges[0]]
        for i in range(1, len(edges)):
            j = 0
            while j < 2:
                if edges[i][0] != ans[j] and edges[i][1] != ans[j]:
                    ans.pop(j)
                    break
                j += 1
            if len(ans) == 1:
                    break
        return ans[0]

        
            
