class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []

        for i in range(len(heights) - 1):
            
            if heights[i + 1] > heights[i]:
                
                diff = heights[i + 1] - heights[i]

                if diff <= bricks:
                    heapq.heappush(heap, -diff)
                    bricks -= diff
                    continue
                if heap and heap[0] * -1 > diff:
                    bricks += -heap[0]
                    heapq.heapreplace(heap, -diff)
                    bricks -= diff

                if ladders:
                    ladders -= 1
                else:
                    return i

        return len(heights) - 1
        
        
                
