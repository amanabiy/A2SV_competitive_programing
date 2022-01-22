# class Solution:
#     def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
#         """ next greater element
#         Time: O(n + m)
#         spame: O(m)
#         where m is the size of nums2 and n is the size of nums1
#         """
#         numIndex = {}
#         ans = []
#         for i, num in enumerate(nums2):
#             numIndex[num] = i
#         for num in nums1:
#             j = numIndex[num]
#             found = False
#             while (j < len(nums2)):
#                 if nums2[j] > num:
#                     ans.append(nums2[j])
#                     found = True
#                     break
#                 j += 1
#             if found == False:
#                 ans.append(-1)
#         return ans

# other optimal solution with stack
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """ next greater element
        Time: O(n + m)
        space: O(m)
        where m is the size of nums2 and n is the size of nums1
        """
        numIndex = {}
        stack = [nums2[0]]
        
        for num in nums2:
            while stack and num > stack[-1]:
                numIndex[stack.pop()] = num
            stack.append(num)
        for i in stack:
            numIndex[i] = -1
        return [numIndex[i] for i in nums1]