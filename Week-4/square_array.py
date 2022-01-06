class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        """ Time: O(nlogn) Space: O(1)"""
        nums = list(map(lambda x: x * x, nums))
        nums.sort()
        return nums