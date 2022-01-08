class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        """ better solution Time: O(nlogn) Space: O(n)"""
        number = sorted(nums)
        less_num = {}
        for index, num in enumerate(number):
            if num not in less_num:
                less_num[num] = index
        return [less_num[num] for num in nums]
# class Solution:
#     def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
#         """ find the smaller numbers from the given index """
#         smaller = []
#         for i in range(len(nums)):
#             count: int = 0
#             for j in range(len(nums)):
#                 if (nums[i] > nums[j]):
#                     count += 1
#             smaller.append(count)
#         return smaller