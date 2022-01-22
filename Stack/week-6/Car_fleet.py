# first solution
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """ Car Fleet
        """
        stack = []
        sp = {}
        for i in range(len(speed)):
            sp[position[i]] = speed[i]
        position.sort()

        for val in position:
            steps = (target - val) / sp[val]
            
            while stack and stack[-1] <= steps:
                stack.pop()    
            stack.append(steps)
        return len(stack)
 
# optimal solution
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """ Car Fleet
        """
        stack = []
        sp = sorted(zip(position, speed), reverse=True)
        for p, s in sp:
            steps = (target - p) / s
            if not stack or stack[-1] < steps:
                stack.append(steps)
        return len(stack)
