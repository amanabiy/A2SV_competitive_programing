class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        """ return the list of the targets indexes """
        targets = []
        for i in range(1, len(nums)):
            temp = i
            while nums[temp - 1] > nums[temp] and temp > 0:
                nums[temp], nums[temp - 1] = nums[temp - 1], nums[temp]
                temp -= 1
        for i in range(len(nums)):
            if nums[i] == target:
                targets.append(i)
        return targets