class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red: List = []
        white: List = []
        blue: List = []
        for color in nums:
            if color == 0:
                red.append(color)
            if color == 1:
                white.append(color)
            if color == 2:
                blue.append(color)
        nums.clear()
        nums.extend(red)
        nums.extend(white)
        nums.extend(blue)