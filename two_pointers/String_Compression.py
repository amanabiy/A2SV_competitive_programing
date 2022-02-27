class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Time: O(n)
        Space: O(1)
        """
        if len(chars) < 2:
            return 1
        
        count = 0
        prev = 0
        curr = 1
        ans = 0
        
        
        while curr < len(chars):
            if chars[prev] == chars[curr]:
                count += 1
            else:
                if count > 0:
                    num = str(count + 1)
                    for i in range(len(num)):
                        chars[prev + i + 1] = num[i]
                    prev += len(num) + 1
                    chars[prev] = chars[curr]
                    count = 0
                else:
                    prev += 1
                    chars[prev] = chars[curr]
            curr += 1

        # if their is a count at the end of the list
        if count > 0:
            num = str(count + 1)
            for i in range(len(num)):
                chars[prev + i + 1] = num[i]
            prev += len(num) + 1
        else:
            prev += 1

        return prev
            
