class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+","-","*","/"]
        stack = []
        for c in tokens:
            if c in operators:
                op1,op2 = int(stack.pop()),int(stack.pop())
                if c == "+":
                    stack.append(op2+op1)
                elif c == "-":
                    stack.append(op2-op1)
                elif c == "*":
                    stack.append(op2*op1)
                elif c == "/":
                    stack.append(int(op2/op1))
            else:
                stack.append(c)
            print(stack)


        return int(stack[0])