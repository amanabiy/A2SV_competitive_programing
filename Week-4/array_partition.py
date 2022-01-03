class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        """ find the min(ai, bi) has maximized value  """
        nums.sort()
        result = 0
        for num in range(len(nums) - 1, -1, -2):
            result += nums[num - 1]
        return result