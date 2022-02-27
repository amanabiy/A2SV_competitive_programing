class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        left = right = 0
        taken = defaultdict(int)
        maxFruits = 0

        
        while right < len(fruits):
            if len(taken) >= 2 and fruits[right] not in taken:
                while len(taken) >= 2 and taken[fruits[left]] > 0:
                    taken[fruits[left]] -= 1
                    if taken[fruits[left]] == 0:
                        del taken[fruits[left]]
                    left += 1
                    
            maxFruits = max(maxFruits, right - left + 1)
            taken[fruits[right]] += 1
            right += 1
        
        return maxFruits 
