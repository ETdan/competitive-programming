class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        answer = temp = 0
        stack = []

        for char in s:
            if char == "(":
                stack.append("(")
            if char == ")":
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(1)
                else:
                    temp=0
                    while stack[-1] != '(':
                        temp+=stack[-1]
                        stack.pop()
                    stack.pop()
                    
                    stack.append(2*temp)
        while stack:
            answer+=stack[-1]
            stack.pop()
    
        

        return answer
