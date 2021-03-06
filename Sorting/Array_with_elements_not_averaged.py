class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """ It will be only average if the left is less and the right is 
        Greater than the middle element
        Time: O(nlogn)
        Space: O(n)
        """
        nums.sort()
        ans = [0] * len(nums)
        odd = 1
        even = 0
        half = int(len(nums) / 2)
        for i in range(half):
            ans[odd] = nums[i]
            ans[even] = nums[half + i]
            odd += 2
            even += 2
        if (len(nums) % 2==1):
            ans[even] = nums[len(nums) - 1]
        return ans


# could have been implemented better like this
# class Solution:
#     def rearrangeArray(self, A: List[int]) -> List[int]:
#         A.sort()
#         for i in range(1, len(A), 2):
#             A[i], A[i - 1] = A[i - 1], A[i]
#         return A 
