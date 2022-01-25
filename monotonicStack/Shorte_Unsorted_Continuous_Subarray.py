class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        """  find the longest unsorted part
        Time: O(n)
        Space: O(2n)
        """
        stackLeft = []
        stackRight = []
        left = len(nums)
        right = -1
        
        
        for i, num in enumerate(nums):
            while stackLeft and nums[stackLeft[-1]] > num:
                left = min(stackLeft.pop(), left)
            stackLeft.append(i)


        for j in range(len(nums) -1, -1 ,-1):
            while stackRight and nums[stackRight[-1]] < nums[j]:
                right = max(stackRight.pop(), right)
            stackRight.append(j)

        return 0 if right == -1 else right - left + 1
            
        
