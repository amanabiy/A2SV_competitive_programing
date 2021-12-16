class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        """ third biggest num """
        firstLargest: int = float("-inf")
        secondLargest: int = float("-inf")
        thirdLargest: int = float("-inf")
        for i in nums:
            if i > firstLargest:
                firstLargest, secondLargest, thirdLargest = i, firstLargest, secondLargest
            elif i > secondLargest and i < firstLargest:
                secondLargest, thirdLargest = i, secondLargest
            elif i > thirdLargest and i < secondLargest and i < firstLargest:
                thirdLargest = i
            else:
                continue
        if thirdLargest != float("-inf"):
            return thirdLargest
        else:
            return firstLargest
        
        