class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Time: O(nlog(n))
        Space: O(k)
        """
        ans = []
        for val in nums:
            if len(ans) < k:
                heapq.heappush(ans, val)
            else:
                if ans[0] < val:
                    heapq.heappop(ans)
                    heapq.heappush(ans, val)
        return ans[0]
