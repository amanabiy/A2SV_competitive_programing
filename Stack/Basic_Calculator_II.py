class Solution:
    def do_calc(self, operands, op):
        """
        Pop from stack and do calculation
        """
        op1 = operands.pop()
        op2 = operands.pop()
        op = '//' if op == '/' else op
        operands.append(eval(f"{op2}"+op+f"{op1}"))

    def calculate(self, s: str) -> int:
        """ Basic calculator
        Time: O(n)
        Space: O(n)
        """
        # define the priority of the operations
        pre = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2
        }
        operands = []
        operation = []
        isPrevDigit = False

        for op in s:
            if op == " ":
                pass
            elif op.isdigit():
                if isPrevDigit:
                    num = operands.pop()
                    operands.append(num+op)
                else:
                    operands.append(op)
                isPrevDigit = True
            else:                
                if not operation or pre[op] > pre[operation[-1]]:
                    operation.append(op)
                else:
                    while operation and pre[op] <= pre[operation[-1]]:
                        self.do_calc(operands, operation.pop())
                    operation.append(op)
                isPrevDigit = False

        # if their are operations not done yet
        while operation:
            self.do_calc(operands, operation.pop())

        return operands[-1]
