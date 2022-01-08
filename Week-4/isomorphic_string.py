class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        """ Time: O(n) Space: O(n)"""
        isomorphic = defaultdict(str)
        for i in range(len(s)):
            if s[i] not in isomorphic and t[i] not in isomorphic.values():
                isomorphic[s[i]] = t[i]
        for index, letter in enumerate(s):
            if isomorphic[letter] != t[index]:
                return False
        return True
        