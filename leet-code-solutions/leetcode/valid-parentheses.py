class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]

        for char in s:
            if char == ')':
                if len(stack) > 0:
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            elif char == '}':
                if len(stack) > 0:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            elif char == ']':
                if len(stack) > 0:
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                        return False
            else:
                stack.append(char)

        return not len(stack)
        