class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        bracket_map = {"}": "{", ")": "(", "]": "["}
        for c in s:
            if c == "}" or c == ")" or c == "]":
                if len(stack) == 0:
                    return False
                elif bracket_map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        if len(stack) == 0:
            return True
        else:
            return False