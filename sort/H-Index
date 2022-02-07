class Solution:
    def hIndex(self, citations: List[int]) -> int:
        """ Find the h-index of different citations
        Time: O(n)
        Space: O(1)
        """
        citations.sort(reverse=True)
        h_index = 0
        for index, num in enumerate(citations):
            if num >= index + 1:
                h_index += 1
            else:
                break
        return h_index
