class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        """ Numbers with longer length are larger and
        if they have equal length compare the digits
        Time: O(nlogn)
        Space: O(n)
        """
        nums.sort(key=lambda num: [len(num), num])
        return nums[-k]


# class Solution:
#     def kthLargestNumber(self, nums: List[str], k: int) -> str:
#         nums.sort(key=lambda x: int(x))
#         return nums[-k]