class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        """ count if the multiplication is already used or not
        Time: O(nlogn)
        Space: O(2n)
        """
        unchanged = []
        changed.sort()
        counter = Counter(changed)
        for i in range(len(changed)):
            if counter[changed[i]] and counter[changed[i] * 2]:                
                if (changed[i] == 0 and counter[0] > 1) or changed[i] != 0:
                    counter[changed[i]*2] -= 1
                    counter[changed[i]] -= 1
                    unchanged.append(changed[i])
        return unchanged if len(unchanged) == len(changed) / 2 else []