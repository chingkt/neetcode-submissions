class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            print("current stack", stack)
            if self.isOperator(token):
                print("operator", token)
                operation = self.getOperation(token)
                res = operation(stack.pop(), stack.pop())
                print("res", res)
                stack.append(res)
            else:
                stack.append(int(token))
        print(stack[-1])
        return stack.pop()

    def isOperator(self, token: str) -> bool:
        return token in set('+-*/')

    def getOperation(self, token: str):
        match token:
            case '+':
                return lambda a, b: b + a
            case '-':
                return lambda a, b: b - a
            case '*':
                return lambda a, b: b * a
            case '/':
                return lambda a, b: int(b / a)