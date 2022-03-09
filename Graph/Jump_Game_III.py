class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        length = len(arr)
        visited = set()
        queue = deque([start])
        visited.add(start)
        
        while queue:
            n = len(queue)
            
            for _ in range(n):
                index = queue.popleft()
                value = arr[index]
                right = value + index
                left = index - value
                
                if value == 0:
                    return True
                
                if right < length and right not in visited:
                    visited.add(right)
                    queue.append(right)
                
                if left >= 0 and left not in visited:
                    visited.add(left)
                    queue.append(left)
    
        return False        
