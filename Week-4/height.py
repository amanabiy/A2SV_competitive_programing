class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """ returns how many are aligned incorrectly"""
        original_pos = heights[:]
        heights.sort()
        count = 0
        for i in range(len(heights)):
            if original_pos[i] != heights[i]:
                count += 1
        return count