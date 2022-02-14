class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        """
        left = [1]
        right = [1]
        ans = []
        for i in range(len(nums) - 1):
            left.append(left[-1] * nums[i])
            right.append(right[-1] * nums[len(nums) -1 -i])

        for x, y in zip(left, right[::-1]):
            ans.append(x * y)
        return ans
