class Solution:
    """
    Space: O(1)
    Time: O(n)
    """
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.reccursionSwap(s, 0, len(s) -1)
    
    def reccursionSwap(self, s, left, right):
        if left >= right:
            return
        s[left], s[right] = s[right], s[left]
        self.reccursionSwap(s, left+1, right-1)
    
def reverseString(s):
    """ reverse  string starting from the last
    Time: O()
    Space: O(n)
    """
    if len(s) == 1:
        return s[-1]
    return s[-1] + reverseString(s[0:-1])


def reverseString2(s):
    """ divide and reverse the string
    Time: O(n^2)
    Space: O(n)
    """
    if len(s) == 1:
        return s[-1]
    middle = len(s) // 2
    return reverseString2(s[middle::]) + reverseString2(s[0:middle])

def reverseList(s):
    """
    """
    if len(s) == 1:
        return [s[-1]]
    middle = len(s) // 2
    return reverseList(s[middle:]) + reverseList(s[0:middle])

if __name__ == "__main__":
    a = [1,2,3,4,5]
    print(a[0:-1])
    print(reverseString("only one at a time"))
    print(reverseString2("split, reverse and combine"))
    print(reverseList(a))