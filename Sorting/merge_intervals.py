class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        merge the duplicate intervals and return the non-overlappint intervals
        Time: O(n)
        Space: O(n)
        """
        intervals.sort()
        index = 0
        ans = [intervals[index]]
        for elem in intervals:
            if elem[0] <= ans[index][1]:
                if elem[1] > ans[index][1]:
                    ans[index][1] = elem[1]
            else:
                ans.append(elem)
                index += 1
        return ans
        

        