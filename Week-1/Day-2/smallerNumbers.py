class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """ find the smaller numbers from the given index """
        smaller = []
        for i in range(len(nums)):
            count: int = 0
            for j in range(len(nums)):
                if (nums[i] > nums[j]):
                    count += 1
            smaller.append(count)
        return smaller