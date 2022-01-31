class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        """
        left = 0
        right = len(height) - 1
        max_area = 0
        for i in range(len(height)):
            area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, area);
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
