class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        """
        Time: O(n)
        Space: O(n)
        """
        ans = []
        i = 0
        for num in pushed:
            ans.append(num)
            while popped and ans and popped[i] == ans[-1]:
                ans.pop()
                i += 1
        return len(ans) == 0
