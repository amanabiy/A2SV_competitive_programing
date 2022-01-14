class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """evaluate """
        calculate = []
        char = {'+', '-', '*', '/'}
        for element in tokens:
            if element not in char:
                calculate.append(element)
            else:
                right = calculate.pop()
                left = calculate.pop()
                calculate.append(eval(f"int({left}{element}{right})"))
        return int(calculate.pop())