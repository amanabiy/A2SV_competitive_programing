class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Time: O(n)
        Space: O(n)
        """
        preSum = [0]
        lastSum = [0]
        n = len(nums)
        i = 0


        while i < n:
            preSum.append(nums[i] + preSum[i])
            lastSum.append(nums[n -1- i] + lastSum[i])
            i += 1
        lastSum = lastSum[::-1]

        i = 0
        while i < n:
            if preSum[i] == lastSum[i+1]:
                return i
            i += 1

        return -1
                
