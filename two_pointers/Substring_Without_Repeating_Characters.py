class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        left = right = 0
        maxLength = 0
        seen = set()
        
        
        while right < len(s):
            if s[right] in seen:
                seen.remove(s[left])
                left += 1
            else:
                seen.add(s[right])
                right += 1
            maxLength = max(maxLength, len(seen))
        
        return maxLength
