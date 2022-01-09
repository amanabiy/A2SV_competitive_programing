class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """ Time: O(n) Space: O(n)"""
        unduplicated = set(nums)
        res = []        
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                print("ap", nums)
                res.append(nums[i])
        for i in range(1, len(nums) + 1):
            if i not in unduplicated:
                res.append(i)
        return res