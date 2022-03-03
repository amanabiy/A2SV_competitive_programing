class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = list(map(lambda x: x*-1, stones))
        heapq.heapify(stones)
        while len(stones) > 1:
            y = heapq.heappop(stones)
            x = heapq.heappop(stones)
            y -= x
            if y != 0:
                heapq.heappush(stones, y)
                y = 0
        return stones[0] * -1 if stones else 0
