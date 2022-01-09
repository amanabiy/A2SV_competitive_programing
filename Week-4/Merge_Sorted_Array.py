class Solution:
    def insertion(self, num, start):
        for i in range(start, 0, -1):
            if num[i] < num[i - 1]:
                num[i], num[i - 1] = num[i - 1], num[i]

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n > 0:
            for num in range(len(nums2)):
                nums1[m] = nums2[num]
                self.insertion(nums1, m)
                m += 1