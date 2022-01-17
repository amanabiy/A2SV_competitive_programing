class MinStack:
    """ Space: O(n) Time: O(1)"""
    def __init__(self):
        self.stack = []        
        self.minum = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minum or val < self.minum[-1]:
            self.minum.append(val)
        else:
            self.minum.append(self.minum[-1])
            
    def pop(self) -> None:
        self.stack.pop()
        self.minum.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minum[-1]
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()