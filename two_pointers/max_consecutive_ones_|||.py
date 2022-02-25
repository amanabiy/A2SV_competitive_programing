class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        maxOnes = 0
        left = 0
        right = 0
        used = 0
        while right < len(nums):
            if nums[right] == 1:
                right += 1
            else:
                if used < k:
                    used += 1
                    right += 1
                else:
                    while nums[left] == 1:
                        left += 1
                    left += 1
                    used -= 1
            maxOnes = max(right - left, maxOnes)
        return maxOnes
            